{
    'name': 'add_product',
    'version': '1.0',
    'summary': 'Extend product and sale.order models with brand information.',
    'depends':  ['product', 'stock', 'sale'],

    'data': [
        'views/product_brand_views.xml',
        'views/inventory_line_views.xml',
        'views/order_line_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
