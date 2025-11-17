from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeFamily(models.Model):
    _name = 'hr.employee.family'

    employee_id = fields.Many2one('hr.employee')
    name = fields.Char()
    phone = fields.Char()
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('husband', 'Husband'),
        ('wife', 'Wife'),
        ('son', 'Son'),
        ('daughter', 'Daughter')
    ])

    _sql_constraints = [('unique_employee_member_name', 'unique(employee_id, name)', 'This employee already has a family member with this name!')]

    @api.constrains('name', 'phone')
    def check_family_fields(self):

        for rec in self:
            # Name Not Empty!
            if not rec.name or rec.name.strip()=="":
                raise ValidationError("Name Can Not Be Empty!")

            # Phone should contain digits only!
            if rec.phone and not rec.phone.isdigit():
                raise ValidationError("Phone Should Contain Digits Only!")