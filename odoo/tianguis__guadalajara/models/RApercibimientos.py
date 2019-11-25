# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class Apercibimientos(models.Model):
    _name = 'r_apercibimientos'
    permisionario = fields.Many2one("permisionario", string = "Permisionario")
    puesto = fields.Many2one("puestos", string = "Puesto")
    motivo = fields.Char (string = "Motivo")
    

    @api.model
    def create(self, vals):
        if vals.get('motivo', False):
            vals['motivo'] = vals.get('motivo', '').upper()
        return super(Apercibimientos, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('motivo', False):
            vals['motivo'] = vals.get('motivo', '').upper()
        return super(Apercibimientos, self).write(vals)

