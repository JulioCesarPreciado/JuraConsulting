# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
colums = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ']

class RTarjetonesFotografia(models.Model):
    _name = 'reporte.tarjetones.fotografia'

    tianguis = fields.Char(string='TIanguis')
    dia = fields.Char(string='Día')
    folio = fields.Integer(string='FOLIO')
    perm = fields.Integer(string='PERM')
    situacion = fields.Char(string='SITUACIÓN')
    nombre = fields.Char(string='NOMBRE')
    giro = fields.Char(string='GIRO')
    linea = fields.Char(string='LINEA')
    inicia = fields.Float(string='INICIA')
    termina = fields.Float(string='TERMINA')
    longitud = fields.Float(string='LONGITUD')
    observaciones = fields.Char(string='OBSERVACIONES')

class ReporteTarjetonesFortografiaXml(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("ENTREGA DE TARJETONES CON FOTOGRAFIA")
        format1 = workbook.add_format({'font_size': 12,'bold': True,'bg_color': '#D3D3D3'})
        format2 = workbook.add_format({'font_size': 12})
        x = 1
        x2 = -1
        col = ""
        col2 = ""
        
        keys = [
            'tianguis',
            'dia',
            'folio',
            'perm',
            'situacion',
            'nombre',
            'giro',
            'linea',
            'inicia',
            'termina',
            'longitud',
            'observaciones'
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

ReporteTarjetonesFortografiaXml('report.tianguis__guadalajara.tarjetones_fotografia_report_xls.xlsx', 'reporte.tarjetones.fotografia')
    
    