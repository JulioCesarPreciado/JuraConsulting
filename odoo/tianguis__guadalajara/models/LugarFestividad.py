# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class LugarFestividad(models.Model):
    _name = 'lugar_festividad'
    festividad = fields.Many2one('c_festividades',string = "Festividad")
    nombre = fields.Char(string="Nombre de el Lugar de la Festividad", required=1)
    ubicacion = fields.Text (string= "Ubicación del Evento")
    largo = fields.Float(string = "Largo")
    ancho = fields.Float(string= "Ancho")
    zona = fields.Many2one('c_zona', string = "Zona Comercial")
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
        return super(LugarFestividad, self).create(vals)
        if vals.get('ubicacion', False):
            vals['ubicacion'] = vals.get('ubicacion', '').upper()
        return super(LugarFestividad, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        return super(LugarFestividad, self).create(vals)
        if vals.get('ubicacion', False):
            vals['ubicacion'] = vals.get('ubicacion', '').upper()
        return super(LugarFestividad, self).create(vals)
