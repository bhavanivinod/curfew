# -*- coding: utf-8 -*-
from odoo import http

# class Curfew(http.Controller):
#     @http.route('/curfew/curfew/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/curfew/curfew/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('curfew.listing', {
#             'root': '/curfew/curfew',
#             'objects': http.request.env['curfew.curfew'].search([]),
#         })

#     @http.route('/curfew/curfew/objects/<model("curfew.curfew"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('curfew.object', {
#             'object': obj
#         })