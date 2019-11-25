# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CMvtoDesc(models.Model):
    _name = 'c_motivodescuento'

    permisionario = fields.Many2one('permisionario')
    puesto = fields.Many2one("puestos")
    vchMotivoDescuento = fields.Char("Motivo Descuento", required=1)
    tynDescuento = fields.Integer("Descuento", default=50, readonly=1)
    estatus = fields.Selection(
        [('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.estatus == 'A':
                name = str(record.tynDescuento) + '% Motivo: ' + record.vchMotivoDescuento
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('vchMotivoDescuento', False):
            vals['vchMotivoDescuento'] = vals.get('vchMotivoDescuento', '').upper()
        return super(CMvtoDesc, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchMotivoDescuento', False):
            vals['vchMotivoDescuento'] = vals.get('vchMotivoDescuento', '').upper()
        return super(CMvtoDesc, self).write(vals)

        
