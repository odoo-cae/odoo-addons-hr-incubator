# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Event(models.Model):
    _inherit = "event.event"

    timesheet_sheet_created = fields.Boolean(
        string="Timesheet Sheets already created before."
    )
