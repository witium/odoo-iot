# -*- coding: utf-8 -*-
{
    'name': "esp8266",

    'summary': """
        Modulo para controlar el SoC esp8266
    """,

    'author': "Miguel Hiciano",
    'website': "https://github.com/MikeHiciano/odoo-iot",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
 
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
}