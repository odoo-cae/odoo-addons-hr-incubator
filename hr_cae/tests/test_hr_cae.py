# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields
from odoo.tests.common import TransactionCase


class TestHRCAE(TransactionCase):
    def test_create_employee_from_applicant(self):
        applicant = self.browse_ref("hr_recruitment.hr_case_salesman0")
        applicant.type_id = self.browse_ref("hr_recruitment.degree_graduate")
        applicant.certificate_date = fields.Date.today()
        applicant.professional_experience = "A lot of experience"
        applicant.equipment = "Pen and paper"
        applicant.title = self.browse_ref("base.res_partner_title_mister")

        applicant.create_employee_from_applicant()
        employee = applicant.emp_id

        self.assertEquals(employee.certificate_id, applicant.type_id)
        self.assertEquals(employee.certificate_date, applicant.certificate_date)
        self.assertEquals(
            employee.professional_experience, applicant.professional_experience
        )
        self.assertEquals(employee.equipment, applicant.equipment)
        self.assertEquals(employee.title, applicant.title)
