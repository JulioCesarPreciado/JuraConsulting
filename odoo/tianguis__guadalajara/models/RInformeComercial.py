# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

class reporte_General(models.Model):
    _name = 'reporte.general'

    folio = fields.Char(string='Folio')
    nombre = fields.Char(string='Nombre')
    giro = fields.Char(string='Giro')
    motivo_descuento = fields.Char(string='Motivo del descuento')
    sexo = fields.Char(string='Sexo')
    lugar = fields.Char(string='Lugar otorgado')
    asistencia_semana = fields.Char(string='Asistencia por semana')
    asistencia_mes = fields.Char(string='')
    