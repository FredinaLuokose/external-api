# -*- coding: utf-8 -*-
# from odoo import http


# class Mydemo(http.Controller):
#     @http.route('/mydemo/mydemo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mydemo/mydemo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mydemo.listing', {
#             'root': '/mydemo/mydemo',
#             'objects': http.request.env['mydemo.mydemo'].search([]),
#         })

#     @http.route('/mydemo/mydemo/objects/<model("mydemo.mydemo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mydemo.object', {
#             'object': obj
#         })

