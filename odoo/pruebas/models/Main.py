# -*- coding: utf-8 -*-

from odoo import models, fields

class Main(models.Model):
    _name = 'main'

    nombre = fields.Char(string='Nombre del Producto/Servicio')
    precio_total = fields.Float(string='Precio Total')