# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
import base64
import pdb

class ReportesRecaudacion(models.Model):
    _name = 'r_recaudacion'

    tianguis = fields.Many2one('c_tianguis', string='Tianguis', placeholder='Seleccione el tianguis')
    fecha_inicial = fields.Date(string='Fecha Inicial', placeholder = 'Seleccione la fecha inicial', required=True)
    fecha_final = fields.Date(string='Fecha Final', placeholder = 'Seleccione la fecha final', required=True)
    recaudador = fields.Many2one('c_recaudador', string='Recaucador', placeholder = 'Seleccione el racaudador')
    dia = fields.Selection([(1, 'LUNES'), (2, 'MARTES'), (3, 'MIERCOLES'), (4, 'JUEVES'), (5, 'VIERNES'), (6, 'SABADO'), (7, 'DOMINGO')], string="Día")

    def run_sql(self, fecha_i, fecha_f, recaudador, dia, tianguis):
        if(recaudador == False and dia == False and tianguis == False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        if(recaudador != False and dia == False and tianguis == False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' AND recaudadorid = " + str(recaudador) + " ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        if(recaudador == False and dia != False and tianguis == False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' AND dia = " + str(dia) + " ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        if(recaudador == False and dia == False and tianguis != False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' AND tianguisid = " + str(tianguis) + " ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        if(recaudador == False and dia != False and tianguis != False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' AND tianguisid = " + str(tianguis) + " AND dia = " + str(dia) + "ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        if(recaudador != False and dia != False and tianguis != False):
            qry = "SELECT * FROM reporte_recaudacion_dia WHERE fecha BETWEEN '" + str(fecha_i) + "' AND ' " + str(fecha_f) + "' AND tianguisid = " + str(tianguis) + " AND dia = " + str(dia) + " AND recuadadorid = " + str(recaudador) + "ORDER BY dia, tianguis, recaudador"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            if(_res != None):
                return _res
            return '-'
        return ' Error: Recaudador: ' + str(recaudador) + ' Tianguis' + str(tianguis) + ' Día: ' + str(dia)
 






