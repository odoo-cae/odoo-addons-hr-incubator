# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


import logging

import phonenumbers
from phonenumbers import PhoneNumberFormat

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


def _format_phone_number(number: str) -> str:
    """Format a given phone number into a standardized one.
    Special case numbers with +33 indicator (france) are rendered
    as national numbers without international prefix."""
    number = phonenumbers.parse(number, "FR")
    formatter = (
        PhoneNumberFormat.NATIONAL
        if number.country_code == 33
        else PhoneNumberFormat.INTERNATIONAL
    )

    return phonenumbers.format_number(number, formatter)


class Employee(models.Model):
    _inherit = "hr.employee"

    users_count = fields.Integer(
        string="Users Count", compute="_compute_users_count"
    )

    @api.model
    def create(self, values):

        if "mobile_phone" in values and values["mobile_phone"]:
            values["mobile_phone"] = _format_phone_number(
                values["mobile_phone"]
            )
        if "work_phone" in values and values["work_phone"]:
            values["work_phone"] = _format_phone_number(values["work_phone"])

        employee = super().create(values)
        if not employee.address_home_id:
            address_home_ids = (
                self.env["hr.employee"].search([]).mapped("address_home_id.id")
            )
            partner = self.env["res.partner"].search(
                [
                    ("email", "!=", False),
                    ("email", "=", employee.work_email),
                    ("is_company", "=", False),
                    ("id", "not in", address_home_ids),
                ],
                limit=1,
            )
            if partner:
                employee.address_home_id = partner
            else:
                employee.address_home_id = self.env["res.partner"].create(
                    {
                        "is_company": False,
                        "name": employee.name,
                        "email": employee.work_email,
                        "phone": employee.work_phone,
                        "mobile": employee.mobile_phone,
                    }
                )
        return employee

    @api.multi
    def write(self, values):
        if "mobile_phone" in values and values["mobile_phone"]:
            values["mobile_phone"] = _format_phone_number(
                values["mobile_phone"]
            )
        if "work_phone" in values and values["work_phone"]:
            values["work_phone"] = _format_phone_number(values["work_phone"])
        return super().write(values)

    @api.multi
    @api.depends("work_email")
    def _compute_users_count(self):
        for employee in self:
            employee.users_count = len(
                self.env["res.users"].search(
                    [("login", "=", employee.work_email)]
                )
            )

    @api.multi
    def create_user_portal_access(self):
        group_id = self.env.ref("base.group_portal").id
        company_id = (
            self.env["res.company"]._company_default_get("res.users").id
        )

        for employee in self:
            if not employee.work_email:
                raise ValidationError(
                    _("An email address is required for employee %s.")
                    % employee.name
                )
            user = self.env["res.users"].search(
                [("login", "=", employee.work_email)], limit=1
            )
            if user:
                user.write({"active": True, "groups_id": [(4, group_id)]})
            else:
                if employee.address_home_id:
                    partner_id = employee.address_home_id
                else:
                    partner_id = self.env["res.partner"].create(
                        {
                            "is_company": False,
                            "name": employee.name,
                            "email": employee.work_email,
                            "phone": employee.work_phone,
                            "mobile": employee.mobile_phone,
                        }
                    )
                user_values = {
                    "partner_id": partner_id.id,
                    "employee_ids": [(6, 0, [employee.id])],
                    "email": employee.work_email,
                    "login": employee.work_email,
                    "phone": employee.work_phone,
                    "mobile": employee.mobile_phone,
                    "groups_id": [(6, 0, [group_id])],
                    "company_id": company_id,
                    "company_ids": [(6, 0, [company_id])],
                }

                user = (
                    self.env["res.users"]
                    .sudo()
                    .with_context(no_reset_password=True)
                    ._create_user_from_template(user_values)
                )

                (
                    user.sudo()
                    .with_context({"create_user": True, "active_test": True})
                    .action_reset_password()
                )
