

{
    'name': "archive_customers",
    'version': '1',
    'summary': """New custom module for testing""",
    'description': """This module records real estate info""",
    'author': "Ahmed Salah ",
    'category': 'Tools',
    'depends': ['base','account','sale_management','purchase','stock'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/customer.xml',
        'wizard/wizard.xml'],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
}
