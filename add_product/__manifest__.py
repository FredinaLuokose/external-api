{
    'name': 'add_product',
    'version': '1.0',
    'summary': 'Extend product and sale.order models with brand information.',
    'depends': ['base', 'sale_management', 'product'],  
    'data': [
        'views/product_brand_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
                'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
