from odoo import api, models


class Contract(models.Model):
    _inherit = "hr.contract"

    @api.multi
    def create_document(self):
        self.ensure_one()
        if self.type_id == self.env.ref(
            "hr_cae_contract.hr_contract_type_cape"
        ):
            action = self.env.ref(
                "coopaname_custom_contract.action_hr_contract_cape"
            ).report_action(self)
        elif (
            self.type_id
            == self.env.ref("coopaname_custom_contract.hr_contract_type_cdi")
            and self.echelon == "main"
        ):
            action = self.env.ref(
                "coopaname_custom_contract.action_hr_contract_cape"
            ).report_action(self)
        else:
            action = self.env.ref(
                "hr_cae_contract.action_hr_contract"
            ).report_action(self)
        return action
