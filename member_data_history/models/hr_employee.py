# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


def format_partner(partner):
    return "({}, {})".format(partner.id, partner.name)


class Employee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def write(self, vals):
        if "address_home_id" in vals:
            if self.address_home_id:
                old_home_address = format_partner(self.address_home_id)
            else:
                old_home_address = False

            partner = self.env["res.partner"].browse(vals.get("address_home_id"))
            new_home_address = format_partner(partner)

            self.env["value.log"].create(
                {
                    "model": "hr.employee",
                    "field": "address_home_id",
                    "previous_value": old_home_address,
                    "new_value": new_home_address,
                }
            )

        if "address_id" in vals:
            if self.address_id:
                old_address = format_partner(self.address_id)
            else:
                old_address = False

            partner = self.env["res.partner"].browse(vals.get("address_id"))
            new_address = format_partner(partner)

            self.env["value.log"].create(
                {
                    "model": "hr.employee",
                    "field": "address_id",
                    "previous_value": old_address,
                    "new_value": new_address,
                }
            )
        return super(Employee, self).write(vals)
