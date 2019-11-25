# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
colums = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ']

class RInformeGeneral(models.Model):
    _name = 'reporte.informe.general'

    tianguis = fields.Char(string='Tianguis')
    zona = fields.Char(string='Zona')
    semana = fields.Char(string='Semana')
    fecha = fields.Date(string='Today')
    linea = fields.Char(string='Linea')
    folio = fields.Integer(string='Folio')
    nombre = fields.Char(string='Nombre')
    giro = fields.Char(string='GIRO')
    motivo_descuento = fields.Char(string='Motivo del descuento')
    sexo = fields.Char(string='SEXO')
    lugar_otorgado = fields.Char(string='Lugar Otrorgado')
    sem1_header = fields.Char(string='semana1 header')
    sem2_header = fields.Char(string='semana2 header')
    sem3_header = fields.Char(string='semana3 header')
    sem4_header = fields.Char(string='semana4 header')
    sem1_line = fields.Char(string='semana1 line')
    sem2_line = fields.Char(string='semana2 line')
    sem3_line = fields.Char(string='semana3 line')
    sem4_line = fields.Char(string='semana4 line')
    asistencia_mensual = fields.Integer(string='sistencia_mensual')
    total_femenino = fields.Integer(string='femenino')
    total_masculino = fields.Char(string='masculino')
    total_generado = fields.Integer(string='total generado')
    sem1_asistence = fields.Integer(string='semana1 asistence')
    sem2_asistence = fields.Integer(string='semana2 asistence')
    sem3_asistence = fields.Integer(string='semana3 asistence')
    sem4_asistence = fields.Integer(string='semana4 asistence')
    mes_asistence = fields.Integer(string='mes asistence')
    lugares_otorgados = fields.Integer(string='lugares otorgados')
    total_puestos = fields.Integer(string='total puestos')
    
class ReporteInformeGeneralXml(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("LISTADO DE GIROS COMERCIALES EN GENERAL")
        format1 = workbook.add_format({'font_size': 12,'bold': True,'bg_color': '#D3D3D3'})
        format2 = workbook.add_format({'font_size': 12})
        x = 1
        x2 = -1
        col = ""
        col2 = ""
        
        keys = [
            'tianguis',
            'zona',
            'semana',
            'fecha',
            'linea',
            'folio',
            'nombre',
            'giro',
            'motivo_descuento',
            'sexo',
            'lugar_otorgado',
            'sem1_header',
            'sem2_header',
            'sem3_header',
            'sem4_header',
            'sem1_line',
            'sem2_line',
            'sem3_line',
            'sem4_line',
            'asistencia_mensual',
            'total_femenino',
            'total_masculino',
            'total_generado',
            'sem1_asistence',
            'sem2_asistence',
            'sem3_asistence',
            'sem4_asistence',
            'mes_asistence',
            'lugares_otorgados',
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

ReporteInformeGeneralXml('report.tianguis__guadalajara.informe_general_report_xls.xlsx', 'reporte.informe.general')    