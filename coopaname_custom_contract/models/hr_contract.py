from odoo import _, api, models
from odoo.exceptions import ValidationError


class Contract(models.Model):
    _inherit = "hr.contract"

    @api.multi  # noqa
    def create_document(self):
        self.ensure_one()
        self.check_existing_document()
        if (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_bonus")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_bonus",
                "Bonus",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cape")
            and self.echelon == "main"
        ):
            self.check_required_fields(
                [
                    "date_start",
                    "date_signature",
                    "turnover_minimum",
                    "hours",
                    "hourly_wage",
                    "wage",
                    "company_id.name",
                    "company_id.company_registry",
                    "company_id.siret",
                    "company_id.ape",
                    "company_id.street",
                    "company_id.city",
                    "company_id.co_ceo.name",
                    "employee_id.name",
                    "employee_id.job_title",
                    "employee_id.birthday",
                    "employee_id.place_of_birth",
                    "employee_id.ssnid",
                    "employee_id.country_id.name",
                    "employee_id.address_home_id.street",
                    "employee_id.address_home_id.city",
                ]
            )
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cape", "CAPE"
            )
        elif (
            self.type_id
            == self.env.ref(
                "hr_cae_contract.hr_contract_type_cape_remuneration"
            )
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cape_remuneration",
                "CAPE Rémuneration",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cape_renewal")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cape_renewal",
                "CAPE Renewal",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cdd")
            and self.echelon == "main"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cdd", "CDD"
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cdi")
            and self.echelon == "main"
            and not self.tag_ids
        ):
            self.check_required_fields(
                [
                    "duration",
                    "date_start",
                    "date_end",
                    "date_signature",
                    "company_id.name",
                    "company_id.siret",
                    "company_id.ape",
                    "company_id.street",
                    "company_id.city",
                    "company_id.co_ceo.name",
                    "employee_id.name",
                    "employee_id.birthday",
                    "employee_id.place_of_birth",
                    "employee_id.ssnid",
                    "employee_id.job_title",
                    "employee_id.address_home_id.street",
                    "employee_id.address_home_id.city",
                    "employee_id.country_id.name",
                    "employee_id.origin_status_id.name",
                ]
            )
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cdi", "CDI"
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cdi")
            and self.echelon == "main"
            and "cadre" in self.tag_ids.mapped("name")
            and "permanent" in self.tag_ids.mapped("name")
        ):
            return self.create_report_action(
                "coopaname_custom_contract."
                "report_hr_cae_contract_cdi_cadre_permanent",
                "CDI Cadre Permanent",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cdi")
            and self.echelon == "main"
            and "cadre" in self.tag_ids.mapped("name")
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cdi_cadre",
                "CDI Cadre",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_cdi")
            and self.echelon == "main"
            and "permanent" in self.tag_ids.mapped("name")
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_cdi_permanent",
                "CDI Permanent",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_firstsalary")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_firstsalary",
                "First Salary",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_internship")
            and self.echelon == "main"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_internship",
                "Internship",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_lwop")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_lwop",
                "Leave Without Pay",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_lwop_resumption")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_lwop_resumption",
                "Leave Without Pay Resumption",
            )
        elif (
            self.type_id
            == self.env.ref(
                "hr_cae_contract.hr_contract_type_salary_evolution"
            )
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_salary_evolution",
                "Salary Evolution",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_salary_reminder")
            and self.echelon == "amendment"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_salary_reminder",
                "Salary Reminder",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_support")
            and self.echelon == "main"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_support",
                "Support",
            )
        elif (
            self.type_id
            == self.env.ref("hr_cae_contract.hr_contract_type_termination")
            and self.echelon == "termination"
        ):
            return self.create_report_action(
                "coopaname_custom_contract.report_hr_cae_contract_termination",
                "Termination",
            )
        else:
            raise ValidationError(
                _("No template defined for this type of contract")
            )
