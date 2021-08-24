# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    stage_wise_task = fields.Text(compute='get_number_of_task')

    def get_number_of_task(self):
        for i in self:
            text = ''
            for type in i.type_ids:
                tasks_length = self.env['project.task'].search([('stage_id', '=', type.id), ('project_id', '=', i.id)]).__len__()
                text += type.name+':' + str(tasks_length)+'<br/>'
            i.stage_wise_task = text