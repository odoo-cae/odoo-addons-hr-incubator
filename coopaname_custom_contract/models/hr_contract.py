from odoo import _, api, models
from odoo.exceptions import ValidationError

from .reference import REFERENCE
from .required_fields import REQUIRED_FIELDS


class Contract(models.Model):
    _inherit = "hr.contract"

    def _get_type_reference(self, contract_type):
        return self.env.ref(REFERENCE[contract_type])

    def _get_required_fields(self, report_name):
        try:
            required_fields = REQUIRED_FIELDS[report_name]
        except KeyError:
            required_fields = None
        return required_fields

    @api.multi
    def create_document(self):  # noqa: C901 (method too complex)
        # This could be made cleaner with a dictionary (for example).
        # Make sure to manage the tags as well.
        self.ensure_one()
        if (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("bonus")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_bonus"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cape")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_cape"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("cape_remuneration")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_cape_remuneration"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("cape_renewal")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_cape_renewal"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cdd")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_cdd"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cdi")
            and not self.tag_ids
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_cdi"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cdi")
            and "cadre" in self.tag_ids.mapped("name")
            and "permanent" in self.tag_ids.mapped("name")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_cdi_cadre_permanent"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cdi")
            and "cadre" in self.tag_ids.mapped("name")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_cdi_cadre"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("cdi")
            and "permanent" in self.tag_ids.mapped("name")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_cdi_permanent"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("firstsalary")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_firstsalary"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("internship")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_internship"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("lwop")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_lwop"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("lwop_resumption")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_lwop_resumption"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("salary_evolution")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_salary_evolution"
            )
        elif (
            self.echelon == "amendment"
            and self.type_id == self._get_type_reference("salary_reminder")
        ):
            report_name = (
                "coopaname_custom_contract."
                "report_hr_cae_contract_salary_reminder"
            )
        elif (
            self.echelon == "main"
            and self.type_id == self._get_type_reference("support")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_support"
            )
        elif (
            self.echelon == "termination"
            and self.type_id == self._get_type_reference("termination")
        ):
            report_name = (
                "coopaname_custom_contract.report_hr_cae_contract_termination"
            )
        else:
            raise ValidationError(
                _("No template defined for this type of contract (and tag).")
            )

        # self.check_required_fields(self._get_required_fields(report_name))
        return self.create_report_action(report_name)
