{
    'name': "HR Custom Advanced",
    'author': "Abdelhameed Mohamed",
    'category': "Human Resources",
    'version': '1.0',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_inherit_view.xml',
        'views/family_view.xml'
    ],
    'installable': True,
    'application': False,
}