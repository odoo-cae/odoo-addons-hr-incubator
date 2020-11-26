from odoo import _, api, models
from odoo.exceptions import ValidationError

from .report_names import REPORT_NAMES


class Contract(models.Model):
    _inherit = "hr.contract"

    def _get_report_names(self):
        report_names = {
            (self.env.ref(type_id).id, echelon): report_name
            for (type_id, echelon), report_name in REPORT_NAMES.items()
        }
        return report_names

    @api.multi
    def create_document(self):
        self.ensure_one()
        report_names = self._get_report_names()

        try:
            report_name = report_names[(self.type_id.id, self.echelon)]
        except KeyError:
            raise ValidationError(
                _("No template defined for contract %s" % self.type_id.name)
            )

        return self.create_report_action(report_name)
