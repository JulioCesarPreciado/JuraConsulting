# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
colums = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ']


class RPermisionarioPermiso(models.Model):
    _name = 'reporte.permisionario.permiso'

    dia = fields.Char(string='Día')
    tianguis = fields.Char(string='Tianguis')
    folio = fields.Integer(string='FOLIO')
    linea = fields.Char(string='LINEA')
    nombre = fields.Char(string='NOMBRE')
    inicia = fields.Float(string='INICIA')
    termina = fields.Float(string='TERMINA')
    longitud = fields.Float(string='LONGITUD')
    semana1 = fields.Char(string='SEM.')
    semana2 = fields.Char(string='SEM.')
    semana3 = fields.Char(string='SEM.')
    semana4 = fields.Char(string='SEM.')

class ReportePermisionarioPermisoXml(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("LISTADO DE PERMISIONARIOS CON PERMISO")
        format1 = workbook.add_format({'font_size': 12,'bold': True,'bg_color': '#D3D3D3'})
        format2 = workbook.add_format({'font_size': 12})
        x = 1
        x2 = -1
        col = ""
        col2 = ""
        
        keys = [
            'dia',
            'tianguis',
            'folio',
            'linea',
            'nombre',
            'inicia',
            'termina',
            'longitud',
            'semana1',
            'semana2',
            'semana3',
            'semana4'
        ]
        row_col_list = []
        for i in data['result']:
            for k in keys:
                if x > len(colums):
					x = 1
					x2 = x2 + 1
					col2 = colums[x2]
                col = col2 + colums[x-1] + "1"
                row_col_list.append(col2 + colums[x-1])
                sheet.write(col, k, format1)
                x = x + 1
            break
        row = 1
        for i in data['result']:
            x = 0
            row_col = ""
            row = row + 1
            for k in keys:
                v = i[k]
                row_col = row_col_list[x] + str(row)
                x = x + 1
                sheet.write(row_col, v, format2)

ReportePermisionarioPermisoXml('report.tianguis__guadalajara.permisionario_permiso_report_xls.xlsx', 'reporte.permisionario.permiso')
    