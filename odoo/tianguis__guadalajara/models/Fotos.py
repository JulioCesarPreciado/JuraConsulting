# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

class Fotos (models.Model):
    _name = 'fotos'
    nombre = fields.Char (string = "Permisionario")
    foto = fields.Binary(string = "Fotografía")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
                result.append((record.id, record.nombre))
        return result
    
    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(Fotos, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(Fotos, self).write(vals)
    
  