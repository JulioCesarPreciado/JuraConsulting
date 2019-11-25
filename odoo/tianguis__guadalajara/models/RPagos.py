# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class Pagos(models.Model):
    _name = 'pagos'
    permisionario = fields.Many2one('permisionario', string = "Permisionario")
    puesto = fields.Many2one('puestos', string= "Puesto")
    concepto = fields.Char(string = "Concepto de Pago", placeholder = "Seleccione el concepto")
    cargo = fields.Float(string = "Cargo")
    abono = fields.Float(string = "Abono")
    saldo_ant = fields.Float(string = "Saldo Anterior")
    saldo_act = fields.Float(string = "Saldo Actual")
    date_action = fields.Datetime()
    saldo = fields.Float(string='Saldo')