# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
colums = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ']

class ReportePuestosPermisionario(models.Model):
    _name = 'reporte.puestos.permisionario'
    permisionario = fields.Char(string='Permisionario')
    direccion = fields.Char(string='Dirección')
    padre = fields.Char(string='Padre')
    madre = fields.Char(string='Madre')
    esposa = fields.Char(string='Esposa')
    hijos = fields.Char(string='Hijos')
    folio = fields.Integer(string='Folio')
    dia = fields.Char(string='Día')
    tianguis = fields.Char(string='Tianguis')
    zona = fields.Char(string='Zona')
    inicia = fields.Boolean(string='Inicia')
    termina = fields.Boolean(string='Termina')
    longitud = fields.Boolean(string='Longitud')
    giro = fields.Char(string='Giro')
    total_puestos = fields.Integer(string='Total de Puestos')
    
class ReportePuestosPermisionarioXml(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("REPORTE DE PUESTOS POR PERMISIONARIO")
        format1 = workbook.add_format({'font_size': 12,'bold': True,'bg_color': '#D3D3D3'})
        format2 = workbook.add_format({'font_size': 12})
        x = 1
        x2 = -1
        col = ""
        col2 = ""
        
        keys = [
            'permisionario',
            'direccion',
            'padre',
            'madre',
            'esposa',
            'hijos',
            'folio',
            'dia',
            'tianguis',
            'zona',
            'inicia',
            'termina',
            'longitud',
            'giro',
            'total_puestos'
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

ReportePuestosPermisionarioXml('report.tianguis__guadalajara.puestos_permisionario_report_xls.xlsx', 'reporte.puestos.permisionario')