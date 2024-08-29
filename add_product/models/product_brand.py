from odoo import fields, models


class ProductBrand(models.Model):
    _name = "product.brand"
    _description = "Product Brand Details"
    _rec_name = "product_brand_name"

    product_brand_logo = fields.Image(width=100, height=100)
    product_brand_name = fields.Char(string="Name", required=True)
    product_brand_description = fields.Text(string="Description")
    product_brand_origin_country = fields.Char(string="Origin Country")
    product_brand_founding_year = fields.Date(string="Founding Year")
    product_brand_ceo_name = fields.Char(string="CEO")
    product_brand_ranking = fields.Integer(string="Brand Ranking")
    product_brand_active = fields.Boolean(string="Active")

