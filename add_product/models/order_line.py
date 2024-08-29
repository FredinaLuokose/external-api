from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand_id = fields.Many2one(
        'product.brand',
        string='Product Brand',
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.product_brand_id = self.product_id.product_tmpl_id.product_brand_id
        else:
            self.product_brand_id = False