from odoo import models, fields

class EmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    personal_code = fields.Char()
    emergency_contact = fields.Char()
    iqama_number = fields.Char()

    family_member_ids = fields.One2many('hr.employee.family', 'employee_id')
