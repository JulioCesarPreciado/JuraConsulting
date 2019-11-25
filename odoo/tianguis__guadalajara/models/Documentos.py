# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class Documentos(models.Model):
    _name = 'documentos'

    permisionario_id = fields.Many2one('permisionario', string='Permisionario')
    nombre = fields.Char("Nombre del archivo")
    documento = fields.Binary(string='Documento')