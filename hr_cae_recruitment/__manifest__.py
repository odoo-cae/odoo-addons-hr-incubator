# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# Copyright 2020
#   Quentin DUPONT <quentin.dupont@grap.coop>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR CAE Recruitment",
    "summary": "Manage recruitment in a CAE.",
    "author": "Coop IT Easy SCRLfs, GRAP",
    "website": "https://www.coopiteasy.be, http://www.grap.coop",
    "category": "Human Resources",
    "version": "12.0.1.3.0",
    "license": "AGPL-3",
    "depends": ["hr_cae", "hr_recruitment"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr.xml",
        "views/hr_applicant.xml",
        "views/hr_employee.xml",
        "views/hr_job.xml",
        "data/data.xml",
    ],
    "installable": True,
    "application": False,
}
