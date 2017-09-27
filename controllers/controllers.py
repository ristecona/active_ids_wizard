# -*- coding: utf-8 -*-
from odoo import http

# class ActiveIdsWizard(http.Controller):
#     @http.route('/active_ids_wizard/active_ids_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/active_ids_wizard/active_ids_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('active_ids_wizard.listing', {
#             'root': '/active_ids_wizard/active_ids_wizard',
#             'objects': http.request.env['active_ids_wizard.active_ids_wizard'].search([]),
#         })

#     @http.route('/active_ids_wizard/active_ids_wizard/objects/<model("active_ids_wizard.active_ids_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('active_ids_wizard.object', {
#             'object': obj
#         })