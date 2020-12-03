# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR CAE Contract",
    "summary": "Manage employee contracts in a CAE.",
    "author": "Coop IT Easy SCRLfs",
    "website": "https://www.coopiteasy.be",
    "category": "Human Resources",
    "version": "12.0.1.4.0",
    "license": "AGPL-3",
    "external_dependencies": {"python": ["dateutil.relativedelta"]},
    "depends": ["hr_cae", "hr_contract"],
    "data": [
        "security/ir.model.access.csv",
        "security/hr_security.xml",
        "data/cron.xml",
        "data/hr_contract_data.xml",
        "wizard/create_amendment_wizard.xml",
        "report/hr_contract.xml",
        "views/hr_contract.xml",
        "views/hr_employee.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
}
