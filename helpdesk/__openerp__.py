# -*- encoding: utf-8 -*-

{
    'name': 'Helpdesk',
    'version': '1.0',
    'category': 'Issues',
    'summary': 'Tickets, Helpdesk',
    'description': """
Incidencias puestos
=========================================
Modulo para seguir las incidencias producidas en los puestos de trabajo
    """,
	"init_xml": [],
    'author': 'Domonte SA',
    'depends': [
        'base',
    ],
    'data': [		
        'res_helpdesk_view.xml',		
		'security/security.xml',
		'security/ir.model.access.csv'
     ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
