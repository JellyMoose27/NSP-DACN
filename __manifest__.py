{
    'name': 'Non-stop Parking',
    'description': 'Hệ thống giữ xe không dừng',
    'version': '1.0',
    'sequence': -1,
    'author': 'BKU Team',
    'category': 'NSP',
    'depends': ['base', 'mail'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'data/module_category.xml',

        'security/security.xml',
        'security/ir.model.access.csv',
        
        'views/role_views.xml',
        'views/vehicle_logs_views.xml',
        'views/vehicle_views.xml',
        'views/card_admin_views.xml',
        'views/card_it_views.xml',
        'views/card_security_views.xml',
        'views/group_views.xml',
        'views/service_discovery_views.xml',
        'views/menu_views.xml',
    ],
    # 'assets': [

    # ],
    'license': 'LGPL-3'
}