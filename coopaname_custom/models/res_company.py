# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    co_ceo = fields.Many2one(
        comodel_name="res.partner", string="Co-CEO", required=False
    )
    signature_scan = fields.Binary(string="Co-CEO signature")
