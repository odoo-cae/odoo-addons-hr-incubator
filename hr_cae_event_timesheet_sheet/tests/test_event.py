# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import tests


class TestEvent(tests.common.TransactionCase):
    def test_create_portal_user_from_contact(self):
        event = self.browse_ref("event.event_0")
        admin_user = self.browse_ref("base.user_admin")
        partner_1 = self.browse_ref("base.res_partner_1")
        partner_2 = self.browse_ref("base.res_partner_2")
        employee = self.browse_ref("hr.employee_al")
        account = self.browse_ref("analytic.analytic_rd_department")
        project = self.browse_ref("project.project_project_2")

        self.assertFalse(
            self.env["res.users"].search([("login", "=", partner_1.email)])
        )
        self.assertFalse(
            self.env["res.users"].search([("login", "=", partner_2.email)])
        )
        self.assertFalse(
            self.env["res.users"].search([("login", "=", employee.work_email)])
        )

        partner_1_user = self.env["res.users"].create(
            {
                "name": partner_1.name,
                "login": partner_1.email,
                "email": partner_1.email,
                "partner_id": partner_1.id,
            }
        )
        partner_2_user = self.env["res.users"].create(
            {
                "name": partner_2.name,
                "login": partner_2.email,
                "email": partner_2.email,
            }
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
                "name": partner_1.name,
                "email": partner_1.email,
                "partner_id": partner_1.id,
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": partner_2.name,
                "email": partner_2.email,
            }
        )
        self.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": employee.name,
                "email": employee.work_email,
                "employee_id": employee.id,
            }
        )

        wizard = (
            self.env["hr.cae.event.to.timesheet.wizard"]
            .with_context({"active_id": event.id})
            .create({"account_id": account.id, "project_id": project.id})
        )

        self.assertTrue(admin_user in wizard.user_ids)
        self.assertTrue(partner_1_user in wizard.user_ids)
        self.assertTrue(partner_2_user in wizard.user_ids)
        self.assertTrue(employee_user in wizard.user_ids)

        wizard.create_timesheet_sheets()

        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", partner_1_user.id)]
            )
        )
        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", partner_2_user.id)]
            )
        )
        self.assertTrue(
            self.env["account.analytic.line"].search(
                [("user_id", "=", employee_user.id)]
            )
        )
