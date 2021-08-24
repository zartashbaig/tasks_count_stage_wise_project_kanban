# -*- coding: utf-8 -*-
# from odoo import http


# class TaskLengthStageWise(http.Controller):
#     @http.route('/task_length_stage_wise/task_length_stage_wise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_length_stage_wise/task_length_stage_wise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_length_stage_wise.listing', {
#             'root': '/task_length_stage_wise/task_length_stage_wise',
#             'objects': http.request.env['task_length_stage_wise.task_length_stage_wise'].search([]),
#         })

#     @http.route('/task_length_stage_wise/task_length_stage_wise/objects/<model("task_length_stage_wise.task_length_stage_wise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_length_stage_wise.object', {
#             'object': obj
#         })
