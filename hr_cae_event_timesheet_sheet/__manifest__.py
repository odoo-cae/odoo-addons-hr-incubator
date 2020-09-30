# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR CAE Event Timesheet Sheet",
    "summary": "Manage Events and Timesheets in a CAE.",
    "author": "Coop IT Easy SCRLfs",
    "website": "https://www.coopiteasy.be",
    "category": "Human Resources",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["hr_timesheet_sheet", "hr_cae_event"],
    "data": ["wizard/event_to_timesheet.xml", "views/event.xml"],
    "demo": [],
    "installable": True,
    "application": False,
}
