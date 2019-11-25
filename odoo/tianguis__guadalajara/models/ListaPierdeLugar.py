# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class ListaPierdeLugar(models.Model):
    _name = "lista_pierde_lugar"

    Permisionario = fields.Char(string = "Permisionario")
    Tianguis = fields.Char(string="Tianguis")
    Fecha = fields.Date(string = "Fecha de la Falta")
    Faltot = fields.Many2one('asistencias', string = "Faltas Totales")
    Falseg = fields.Many2one('asistencias', string = "Faltas Totales")
    FechaPierde = fields.Datetime(string  = "Fecha Pierde Lugar")
    smlGiro = fields.Char(string="Giro Comercial")
    
