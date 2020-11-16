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
        "report/hr_contract_cape.xml",
        "report/hr_contract_cdi.xml",
        "report/reports.xml",
    ],
    "demo": [],
    "external_dependencies": {"python": ["phonenumbers"]},
    "installable": True,
}
