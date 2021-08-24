# -*- coding: utf-8 -*-
{
    'name': "Stage wise tasks counter ",

    'summary': """
       This odoo app helps to show number of tasks in each stage in project kanban view.""",

    'description': """
        This odoo app helps to show number of tasks in each stage in project kanban view.
    """,

    "author": "Cybat",
    "website": "https://www.cybat.net",
    "price": 0.0,
    "currency": 'EUR',
    'version': '14.0.0.1',
    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
}
