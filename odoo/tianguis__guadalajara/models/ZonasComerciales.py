# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class ZonasComerciales(models.Model):
    _name = 'c_zona'
    nombre = fields.Char(string="Nombre", required=1)
    costo = fields.Float(string ="Cuota p/Día")
    estatus = fields.Selection([('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if(record.estatus == 'A'):
                result.append((record.id, record.nombre))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(ZonasComerciales, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(ZonasComerciales, self).write(vals)