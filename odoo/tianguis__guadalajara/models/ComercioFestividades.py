# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class ComercioFestividades(models.Model):
    _name = "c_comercio_festividades"
    estatus = fields.Selection([('A', 'Activo'), ('C', 'Cancelado')], string="Estatus",  default='A') 
    giro = fields.Char(string = "Giro Comercial")
    tipo = fields.Selection(
        [(1, 'COMIDA'), (2, 'COMERCIO')], string='Género', required=1)

    @api.multi
    def name_get(self):
        result = []
        for row in self:
            name = row.giro 
            result.append((row.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('giro', False):
            vals['giro'] = vals.get('giro', '').upper()
        return super(ComercioFestividades, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('giro', False):
            vals['giro'] = vals.get('giro', '').upper()
        return super(ComercioFestividades, self).write(vals)

