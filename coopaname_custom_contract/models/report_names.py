# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

BONUS = "hr_cae_contract.hr_contract_type_bonus"
CAPE = "hr_cae_contract.hr_contract_type_cape"
CAPE_REMUNERATION = "hr_cae_contract.hr_contract_type_cape_remuneration"
CAPE_RENEWAL = "hr_cae_contract.hr_contract_type_cape_renewal"
CDD = "hr_cae_contract.hr_contract_type_cdd"
CDI = "hr_cae_contract.hr_contract_type_cdi"
FIRSTSALARY = "hr_cae_contract.hr_contract_type_firstsalary"
INTERNSHIP = "hr_cae_contract.hr_contract_type_internship"
LWOP = "hr_cae_contract.hr_contract_type_lwop"
LWOP_RESUMPTION = "hr_cae_contract.hr_contract_type_lwop_resumption"
SALARY_EVOLUTION = "hr_cae_contract.hr_contract_type_salary_evolution"
SALARY_REMINDER = "hr_cae_contract.hr_contract_type_salary_reminder"
SUPPORT = "hr_cae_contract.hr_contract_type_support"
TERMINATION = "hr_cae_contract.hr_contract_type_termination"

CONTRACT_BONUS = "coopaname_custom_contract.report_hr_cae_contract_bonus"
CONTRACT_CAPE = "coopaname_custom_contract.report_hr_cae_contract_cape"
CONTRACT_CAPE_REMUNERATION = (
    "coopaname_custom_contract.report_hr_cae_contract_cape_remuneration"
)
CONTRACT_CAPE_RENEWAL = (
    "coopaname_custom_contract.report_hr_cae_contract_cape_renewal"
)
CONTRACT_CDD = "coopaname_custom_contract.report_hr_cae_contract_cdd"
CONTRACT_CDI = "coopaname_custom_contract.report_hr_cae_contract_cdi"
CONTRACT_CDI_CADRE_PERMANENT = (
    "coopaname_custom_contract.report_hr_cae_contract_cdi_cadre_permanent"
)
CONTRACT_CDI_CADRE = (
    "coopaname_custom_contract.report_hr_cae_contract_cdi_cadre"
)
CONTRACT_CDI_PERMANENT = (
    "coopaname_custom_contract.report_hr_cae_contract_cdi_permanent"
)
CONTRACT_FIRSTSALARY = (
    "coopaname_custom_contract.report_hr_cae_contract_firstsalary"
)
CONTRACT_INTERNSHIP = (
    "coopaname_custom_contract.report_hr_cae_contract_internship"
)
CONTRACT_LWOP = "coopaname_custom_contract.report_hr_cae_contract_lwop"
CONTRACT_LWOP_RESUMPTION = (
    "coopaname_custom_contract.report_hr_cae_contract_lwop_resumption"
)
CONTRACT_SALARY_EVOLUTION = (
    "coopaname_custom_contract.report_hr_cae_contract_salary_evolution"
)
CONTRACT_SALARY_REMINDER = (
    "coopaname_custom_contract.report_hr_cae_contract_salary_reminder"
)
CONTRACT_SUPPORT = "coopaname_custom_contract.report_hr_cae_contract_support"
CONTRACT_TERMINATION = (
    "coopaname_custom_contract.report_hr_cae_contract_termination"
)

REPORT_NAMES = {
    (BONUS, "amendment"): CONTRACT_BONUS,
    (CAPE, "main"): CONTRACT_CAPE,
    (CAPE_REMUNERATION, "amendment"): CONTRACT_CAPE_REMUNERATION,
    (CAPE_RENEWAL, "amendment"): CONTRACT_CAPE_RENEWAL,
    (CDD, "main"): CONTRACT_CDD,
    (CDI, "main"): CONTRACT_CDI,
    # (CDI, "main"): CONTRACT_CDI_CADRE_PERMANENT,
    # (CDI, "main"): CONTRACT_CDI_CADRE,
    # (CDI, "main"): CONTRACT_CDI_PERMANENT,
    (FIRSTSALARY, "amendment"): CONTRACT_FIRSTSALARY,
    (INTERNSHIP, "main"): CONTRACT_INTERNSHIP,
    (LWOP, "amendment"): CONTRACT_LWOP,
    (LWOP_RESUMPTION, "amendment"): CONTRACT_LWOP_RESUMPTION,
    (SALARY_EVOLUTION, "amendment"): CONTRACT_SALARY_EVOLUTION,
    (SALARY_REMINDER, "amendment"): CONTRACT_SALARY_REMINDER,
    (SUPPORT, "main"): CONTRACT_SUPPORT,
    (TERMINATION, "termination"): CONTRACT_TERMINATION,
}
