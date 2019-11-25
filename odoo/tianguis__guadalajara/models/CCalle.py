# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CCalle(models.Model):
    _name = 'c_calles'

    vchCalle = fields.Char("Calle")
    #smlTianguis = fields.Many2one('c_tianguis', string='Tianguis')
    smlLongitud = fields.Float('Longitud', default=0)
    iCalleInicio = fields.Many2one("c_calles", string="Calle Inicio")
    iCalleFinal = fields.Many2one("c_calles", string='Calle Final')
    estatus = fields.Selection([('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.estatus == 'A':
                name = record.vchCalle
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('vchCalle', False):
            vals['vchCalle'] = vals.get('vchCalle', '').upper()
        return super(CCalle, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchCalle', False):
            vals['vchCalle'] = vals.get('vchCalle', '').upper()
        return super(CCalle, self).write(vals)
