# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class JuegosMecanicos(models.Model):
    _name = "c_juegos_mecanicos"

    estatus = fields.Selection([('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A') 
    nombre = fields.Char(string='Nombre del Juego')
    
    @api.multi
    def name_get(self):
        result = []
        for row in self:
            name = row.nombre
            result.append((row.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(JuegosMecanicos, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(JuegosMecanicos, self).write(vals)
