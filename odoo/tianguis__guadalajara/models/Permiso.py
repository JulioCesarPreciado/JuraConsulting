# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
from datetime import datetime, date


class Permiso(models.Model):
    _name = 'permisos'

    FolioAnterior = fields.Integer(string='Folio Anterior')
    iPERMISIO = fields.Many2one(
        'permisionario', string='Permisionario', required=1)
    Puesto = fields.Many2one('puestos', string='Puesto')
    FechaMov = fields.Date(string='Fecha de Movimiento',
                           default=datetime.today())
    Movimiento = fields.Many2one('c_movimientos_permisos', string='Movimiento')
    FechaInicial = fields.Date(string='Fecha Inicial')
    DiasPagar = fields.Integer(string='Dias a Pagar')
    FechaTermino = fields.Date(string='Fecha Termino')
    CuotaDiaria = fields.Float(string='Couta Diaria')
    Monto = fields.Float(string='Monto')
    Comentario = fields.Text(string='Comentario')
    estatus = fields.Selection([('A', 'ACTIVO'), ('C', 'CANCELADO')])

    @api.onchange('FechaInicial', 'FechaTermino', 'CuotaDiaria')
    def onchange_field(self):
        if self.FechaInicial or self.FechaTermino or self.CuotaDiaria:
            if self.FechaInicial < self.FechaTermino:
                d1 = datetime.strptime(self.FechaTermino, '%Y-%m-%d')
                d2 = datetime.strptime(self.FechaInicial, '%Y-%m-%d')
                delta = d1.date() - d2.date() 
                self.DiasPagar = delta.days
                # este valor se debe de sacar de la tabla configuración
                self.Monto = self.DiasPagar * self.CuotaDiaria


class CMovimientosPermisos(models.Model):
    _name = 'c_movimientos_permisos'

    Nombre = fields.Char(string='Nombre')
    Descripcion = fields.Text(string='Descripción')
    Cuesta = fields.Char(string='Cuesta')
    Renueva = fields.Char(string='Renueva')
    Afecta = fields.Char(string='Afecta')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = record.Nombre
            result.append((record.id, name))
        return result
