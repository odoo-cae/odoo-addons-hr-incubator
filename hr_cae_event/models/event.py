# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.tools.translate import html_translate


class EventType(models.Model):
    _inherit = "event.type"

    description = fields.Html(
        string="Description",
        oldname="note",
        translate=html_translate,
        sanitize_attributes=False,
        readonly=False,
    )


class Event(models.Model):
    _inherit = "event.event"

    department_id = fields.Many2one("hr.department", string="Department")
    duration = fields.Float(
        string="Duration",
        compute="_compute_duration",
        store=True,
        help="hours",
    )
    co_organizer_id = fields.Many2one("res.partner", string="Co-Organizer")
    state = fields.Selection(readonly=False)

    @api.depends("date_begin", "date_end")
    @api.multi
    def _compute_duration(self):
        for event in self:
            if event.date_begin and event.date_end:
                duration = (
                    event.date_end - event.date_begin
                ).total_seconds() / 3600
            else:
                duration = False
            event.duration = duration

    @api.onchange("event_type_id")
    def _onchange_type(self):
        res = super()._onchange_type()

        if self.event_type_id.description:
            self.description = self.event_type_id.description

        return res

    @api.multi
    def confirm_registrations(self):
        for event in self:
            for registration in event.registration_ids:
                registration.confirm_registration()


class EventRegistration(models.Model):
    _inherit = "event.registration"

    employee_id = fields.Many2one(
        comodel_name="hr.employee", string="Employee", required=False
    )
    state = fields.Selection(readonly=False)

    @api.onchange("employee_id")
    def _onchange_employee_id(self):
        if self.employee_id:
            self.name = self.employee_id.name or self.name
            self.email = self.employee_id.work_email or self.email
            self.phone = self.employee_id.work_phone or self.phone
            self.partner_id = self.employee_id.address_home_id or False
            # Note that the partner is overwritten with False if not found,
            # to prevent inconsistency between partner and employee

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id:
            contact_id = self.partner_id.address_get().get("contact", False)
            if contact_id:
                contact = self.env["res.partner"].browse(contact_id)
                employees = self.env["hr.employee"].search(
                    [("address_home_id", "=", contact.id)]
                )
                if employees:
                    self.employee_id = employees[0] or False
                else:
                    self.employee_id = False
            else:
                self.employee_id = False
                # Note that the employee is overwritten with False if not found,
                # to prevent inconsistency between partner and employee
