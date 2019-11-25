# -*- coding: utf-8 -*-
from odoo import http

# class TianguisGuadalajara(http.Controller):
#     @http.route('/tianguis__guadalajara/tianguis__guadalajara/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tianguis__guadalajara/tianguis__guadalajara/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tianguis__guadalajara.listing', {
#             'root': '/tianguis__guadalajara/tianguis__guadalajara',
#             'objects': http.request.env['tianguis__guadalajara.tianguis__guadalajara'].search([]),
#         })

#     @http.route('/tianguis__guadalajara/tianguis__guadalajara/objects/<model("tianguis__guadalajara.tianguis__guadalajara"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tianguis__guadalajara.object', {
#             'object': obj
#         })