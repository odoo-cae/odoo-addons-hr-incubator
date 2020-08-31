# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class EventRegistration(models.Model):
    _inherit = "event.registration"

    event_type_id = fields.Many2one(
        related="event_id.event_type_id", store=True
    )
    duration = fields.Float(
        string="Duration", related="event_id.duration", store=True
    )
