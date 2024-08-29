from odoo import fields, models, api


class StockPickingLine(models.Model):
    _inherit = "stock.move"

    product_brand_id = fields.Many2one(
        'product.brand',
        string='Product Brand',
        compute='_compute_product_brand',
        # store=True,
    )

    @api.depends('product_id')
    def _compute_product_brand(self):
        for line in self:
            if line.product_id:
                line.product_brand_id = line.product_id.product_tmpl_id.product_brand_id
            else:
                line.product_brand_id = False

