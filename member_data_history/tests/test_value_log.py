# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import tests


@tests.tagged("access_rights")
class TestValueLog(tests.common.TransactionCase):
    def test_log_contract_type_start_end(self):
        contract = self.env["hr.contract"].create(
            {
                "name": "test contract",
                "type_id": self.ref("hr_contract.hr_contract_type_emp"),
                "date_start": "2019-10-12",
                "wage": 2000,
            }
        )

        contract.date_start = "2019-11-13"
        contract.date_end = "2021-11-23"
        contract.type_id = self.ref("hr_contract.hr_contract_type_wrkr")

        log = self.env["value.log"].search(
            [
                ("model", "=", "hr.contract"),
                ("field", "=", "date_start"),
                ("previous_value", "=", "2019-10-12"),
                ("new_value", "=", "2019-11-13"),
            ]
        )
        self.assertTrue(log)

        log = self.env["value.log"].search(
            [
                ("model", "=", "hr.contract"),
                ("field", "=", "date_end"),
                ("previous_value", "=", False),
                ("new_value", "=", "2021-11-23"),
            ]
        )
        self.assertTrue(log)

        old_type = self.browse_ref("hr_contract.hr_contract_type_emp")
        new_type = self.browse_ref("hr_contract.hr_contract_type_wrkr")
        log = self.env["value.log"].search(
            [
                ("model", "=", "hr.contract"),
                ("field", "=", "type_id"),
                ("previous_value", "=", old_type.name),
                ("new_value", "=", new_type.name),
            ]
        )
        self.assertTrue(log)

    def test_log_partner_zip_code(self):
        partner = self.browse_ref("base.res_partner_1")
        old_zip = partner.zip
        partner.zip = "4100"

        log = self.env["value.log"].search(
            [
                ("model", "=", "res.partner"),
                ("field", "=", "zip"),
                ("previous_value", "=", str(old_zip)),
                ("previous_value", "=", str(old_zip)),
                ("new_value", "=", "4100"),
            ]
        )

        self.assertTrue(log)
