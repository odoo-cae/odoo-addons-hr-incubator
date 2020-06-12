# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import tests


class TestEvent(tests.common.TransactionCase):
    def test_create_timesheet_line_for_event_admin_user(self):
        event = self.browse_ref("event.event_0")
        admin_user = self.browse_ref("base.user_admin")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertTrue(admin_user in wizard.user_ids)

        wizard.create_account_analytic_line()

        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", admin_user.id)]
            )
        )

    def test_create_timesheet_line_for_event_partner(self):
        event = self.browse_ref("event.event_0")
        partner = self.browse_ref("base.res_partner_1")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        self.assertFalse(
            self.env["res.users"].search([("login", "=", partner.email)])
        )

        partner_user = self.env["res.users"].create(
            {
                "name": partner.name,
                "login": partner.email,
                "email": partner.email,
                "partner_id": partner.id,
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": partner.name,
                "email": partner.email,
                "partner_id": partner.id,
                "state": "done",
            }
        )

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertTrue(partner_user in wizard.user_ids)

        wizard.create_account_analytic_line()

        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", partner_user.id)]
            )
        )

    def test_create_timesheet_line_for_event_employee(self):
        event = self.browse_ref("event.event_0")
        employee = self.browse_ref("hr.employee_al")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        self.assertFalse(
            self.env["res.users"].search([("login", "=", employee.work_email)])
        )

        employee_user = self.env["res.users"].create(
            {
                "name": employee.name,
                "login": employee.work_email,
                "email": employee.work_email,
                "employee_ids": [(6, 0, [employee.id])],
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": employee.name,
                "email": employee.work_email,
                "employee_id": employee.id,
                "state": "done",
            }
        )

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertTrue(employee_user in wizard.user_ids)

        wizard.create_account_analytic_line()

        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", employee_user.id)]
            )
        )

    def test_create_timesheet_line_for_event_email(self):
        event = self.browse_ref("event.event_0")
        partner = self.browse_ref("base.res_partner_1")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        self.assertFalse(
            self.env["res.users"].search([("login", "=", partner.email)])
        )

        partner_user = self.env["res.users"].create(
            {
                "name": partner.name,
                "login": partner.email,
                "email": partner.email,
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": partner.name,
                "email": partner.email,
                "state": "done",
            }
        )  # no partner or employee linked here, only email

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertTrue(partner_user in wizard.user_ids)

        wizard.create_account_analytic_line()

        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", partner_user.id)]
            )
        )

    def test_dont_find_user_if_not_registration_done(self):
        event = self.browse_ref("event.event_0")
        partner = self.browse_ref("base.res_partner_1")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        self.assertFalse(
            self.env["res.users"].search([("login", "=", partner.email)])
        )

        partner_user = self.env["res.users"].create(
            {
                "name": partner.name,
                "login": partner.email,
                "email": partner.email,
                "partner_id": partner.id,
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": partner.name,
                "email": partner.email,
                "partner_id": partner.id,
                "state": "open",
            }
        )

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertFalse(partner_user in wizard.user_ids)
