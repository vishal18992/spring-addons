# -*- coding: utf-8 -*-
# Part of Spring Financial. See LICENSE file for full copyright and licensing details.


{
    'name': 'Spring CRM',
    'version': '16.0.0.1',
    'category': 'Sales/CRM',
    'sequence': 1,
    'summary': '',
    'website': 'https://www.springfinancial.ca/',
    'depends': [
        'crm',
    ],
    'data': [
        "data/crm_stage_data.xml",
        "views/crm_lead_views.xml",
        "views/crm_stage_views.xml"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
