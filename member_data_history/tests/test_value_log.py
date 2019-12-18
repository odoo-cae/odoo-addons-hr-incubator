# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import tests


@tests.tagged("access_rights")
class TestValueLog(tests.common.TransactionCase):
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
