from odoo import models, fields

class EmployeeInherit(models.Model):
    _inherit = 'hr.employee' # inherit from model hr.employee

    personal_code = fields.Char()
    emergency_contact = fields.Char()
    iqama_number = fields.Char()
