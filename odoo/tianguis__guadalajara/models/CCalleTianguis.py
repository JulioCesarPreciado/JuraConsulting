# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CCalleTianguis(models.Model):
    _name = 'c_calles_tianguis'

    iCallesTianguis = fields.Many2one('c_calles', string='Calles del Tianguis')
    smlTianguis = fields.Many2one('c_tianguis', string='Tianguis')
    estatus = fields.Selection([('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.estatus == 'A':
                for calles in record.iCallesTianguis:
                    name = str(calles.vchCalle)
                    result.append((record.id, name))
        return result
