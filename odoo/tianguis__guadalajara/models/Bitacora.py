# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class Bitacora(models.Model):
    _name = 'bitacora'
    Operacion = fields.Char(string='Operación')
    Tabla = fields.Char(string='Tabla')
    Usuario = fields.Char(string='Usuario')
    dttFechaBitacora = fields.Datetime("Fecha del Movimiento")
   
    @api.model
    def create(self, vals):
        if vals.get('Operacion', False):
            vals['Operacion'] = vals.get('Operacion', '').upper()
        if vals.get('Tabla', False):
            vals['Tabla'] = vals.get('Tabla', '').upper()
        if vals.get('Operacion', False):
            vals['Operacion'] = vals.get('Operacion', '').upper()
        return super(Bitacora, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('Operacion', False):
            vals['Operacion'] = vals.get('Operacion', '').upper()
        if vals.get('Tabla', False):
            vals['Tabla'] = vals.get('Tabla', '').upper()
        if vals.get('Usuario', False):
            vals['Usuario'] = vals.get('Usuario', '').upper()
        return super(Bitacora, self).write(vals)
