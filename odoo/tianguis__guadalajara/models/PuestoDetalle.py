# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PuestoDetalle(models.Model):
    _name = 'puesto_detalle'
    id_permisionario = fields.Many2one('permisionario', string = "Permisionario")
    id_puesto = fields.Many2one('puestos', string = "Puestos")
    id_tianguis = fields.Many2one('c_tianguis', string ="Tianguis")
    id_descuento = fields.Many2one('c_motivodescuento', string = "Motivo Descuento")
    id_apercibimientos= fields.One2many("r_apercibimientos", "permisionario", string=".")
    id_recaudador = fields.Many2one('c_recaudador', string = "Recaudador")
    id_administrador = fields.Many2one('c_administrador', string = "Recaudador")
    id_pago = fields.Many2one('pagos', string = "Pagos")

    fecha = fields.Date(string = "Fecha")
    numero_semana = fields.Integer(string = "No.Semana")

    costo_sin_descuento = fields.Float(string = "Costo Neto")
    costo_descuento = fields.Float("Descuento",default = 0)
    costo_total = fields.Float("Costo Total", defualt = 0)
   

    asistencia = fields.Boolean(string = "Asistencias")
    faltas_consecutivas = fields.Integer(string = "Injustificaciones")
    puntos = fields.Boolean(string = "Asistencias")

    concepto = fields.Selection([('saldo', 'Saldo'), ('efectivo', 'Efectivo'), ('ambos','Saldo y Efectivo'), ('abono','Abono')], string="Concepto de Pago")
    pago_efectivo = fields.Float(string = "Pago en Efectivo",default = 0)
    pago_saldo = fields.Float(string="Pago con Saldo",default = 0)
    pago_ambos = fields.Many2one
    #saldo = fields.Many2one(string= "Saldo Restante", default = 0)


