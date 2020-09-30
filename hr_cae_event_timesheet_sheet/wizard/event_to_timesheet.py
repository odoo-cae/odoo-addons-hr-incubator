# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class EventToTimesheet(models.TransientModel):
    _name = "hr.cae.event.to.timesheet.wizard"
    _description = "Event to Timesheet"

    name = fields.Char(name="Description", required=True)
    date = fields.Date(string="Date", required=True)
    account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        required=True,
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        domain=[("allow_timesheets", "=", True)],
    )
    task_id = fields.Many2one(comodel_name="project.task", string="Task")
    user_ids = fields.Many2many(
        comodel_name="res.users", string="Users", required=True
    )
    duration = fields.Float(name="Duration")

    timesheet_sheet_created = fields.Boolean(
        string="Timesheet Sheets created before."
    )

    @api.model
    def default_get(self, field_names):
        defaults = super().default_get(field_names)
        event = self.env["event.event"].browse(self.env.context["active_id"])
        registrations = self.env["event.registration"].search(
            [("event_id", "=", event.id), ("state", "=", "done")]
        )
        users = self.env["res.users"]
        for registration in registrations:
            if registration.employee_id and registration.employee_id.user_id:
                users |= registration.employee_id.user_id
            elif registration.partner_id and registration.partner_id.user_id:
                users |= registration.partner_id.user_id
            else:
                users_same_email = self.env["res.users"].search(
                    [("email", "=", registration.email)]
                )
                if users_same_email:
                    users |= users_same_email[0]
        users |= event.user_id
        defaults["name"] = event.name
        defaults["date"] = event.date_begin
        defaults["duration"] = event.duration
        defaults["user_ids"] = [(6, 0, users.ids)]
        defaults["timesheet_sheet_created"] = event.timesheet_sheet_created
        return defaults

    @api.multi
    def create_account_analytic_line(self):
        self.ensure_one()

        for user in self.user_ids:
            self.env["account.analytic.line"].create(
                {
                    "name": self.name,
                    "date": self.date,
                    "account_id": self.account_id.id,
                    "project_id": self.project_id.id,
                    "task_id": self.task_id.id,
                    "user_id": user.id,
                    "unit_amount": self.duration,
                }
            )

        event = self.env["event.event"].browse(self.env.context["active_id"])
        event.timesheet_sheet_created = True

        return True
