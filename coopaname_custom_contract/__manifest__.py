# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Coopaname Custom Contract",
    "summary": """
        Customization of Contracts specific to Coopaname use case.
    """,
    "license": "AGPL-3",
    "author": "Coop IT Easy SCRLfs",
    "website": "https://www.coopiteasy.be",
    "category": "Human Resources",
    "version": "12.0.1.0.0",
    "depends": ["coopaname_custom"],
    "data": [
        "report/hr_contract_bonus.xml",
        "report/hr_contract_cape.xml",
        "report/hr_contract_cape_remuneration.xml",
        "report/hr_contract_cape_renewal.xml",
        "report/hr_contract_cdd.xml",
        "report/hr_contract_cdi.xml",
        "report/hr_contract_cdi_cadre.xml",
        "report/hr_contract_cdi_cadre_permanent.xml",
        "report/hr_contract_cdi_permanent.xml",
        "report/hr_contract_firstsalary.xml",
        "report/hr_contract_internship.xml",
        "report/hr_contract_lwop.xml",
        "report/hr_contract_lwop_resumption.xml",
        "report/hr_contract_salary_evolution.xml",
        "report/hr_contract_salary_reminder.xml",
        "report/hr_contract_support.xml",
        "report/hr_contract_termination.xml",
    ],
    "demo": [],
    "external_dependencies": {"python": ["phonenumbers"]},
    "installable": True,
}
