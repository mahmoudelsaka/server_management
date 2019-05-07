# -*- coding: utf-8 -*-
{
    'name': 'Server Management',
    'version': '11.0',
    'category': 'Employee',
    'description': """
Managing Company's Servers:
* Server Management Menu: Human Resources >> Server Management >> Server Management
* Server Management Groups configurable from user profile: Server Access: Limited and Server Access: Full
    """,
    'author': 'Rightechs Solutions',
    'website': 'rightechs.net',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir_security.xml',
        'security/ir.model.access.csv',
        'views/server_view.xml',
        'views/database_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
