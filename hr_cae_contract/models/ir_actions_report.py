from odoo import fields, models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    temporary_action = fields.Boolean(string="Temporary action")
