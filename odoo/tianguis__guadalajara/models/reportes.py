# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,timedelta 
import base64
import pdb

class getReportToRender(models.Model):
    _name = 'report.render'

    module = fields.Selection(string='Selecciona el modulo', selection=[('tianguis', 'Tianguis'), ('espacios', 'Espacios Abiertos'),], default='tianguis')
    report_tianguis = fields.Selection(string='Tianguis', selection=[('informe_general', 'INFORME GENERAL'),
     ('giros_comerciales', 'LISTADO DE GIROS COMERCIALES EN GENERAL'),
     ('puesto_permisionario', 'REPORTE DE PUESTOS POR PERMISIONARIO'),
     ('permisionario_permiso', 'LISTADO DE PERMISIONARIOS CON PERMISO'),
     ('tarjetones_fotografia','ENTREGA DE TARJETONES CON FOTOGRAFÍA')])
    report_espacios = fields.Selection(string='Espacios Abiertos', selection=[('solicitantes', 'Solicitantes'),])
    report_date_from = fields.Date(string='Fecha Inicio de Reporte', required=True)
    report_date_to = fields.Date(string='Fecha Final de Reporte', required = True)
    
    @api.multi
    def get_report_render(self):
        if self.report_tianguis and self.report_date_from and self.report_date_to:
            if self.report_tianguis == 'informe_general':
                datas = {}
                datas = {
                    'ids': [1],
                    'model': 'reporte.informe.general',
                    }
                return {
                    'type':'ir.actions.report.xml',
                    'report_name':'tianguis__guadalajara.reporte_informe_general',
                    'datas':datas,
                    }
            elif self.report_tianguis == 'giros_comerciales':
                datas = {}
                datas = {
                    'ids': [1],
                    'model': 'reporte.giros.comerciales',
                    }
                return {
                    'type':'ir.actions.report.xml',
                    'report_name':'tianguis__guadalajara.reporte_giros_comerciales',
                    'datas':datas,
                    }
            elif self.report_tianguis == 'puesto_permisionario':
                datas = {}
                datas = {
                    'ids': [1],
                    'model': 'reporte.puestos.permisionario',
                    }
                return {
                    'type':'ir.actions.report.xml',
                    'report_name':'tianguis__guadalajara.reporte_puestos_permisionario',
                    'datas':datas,
                    }
            elif self.report_tianguis == 'permisionario_permiso':
                datas = {}
                datas = {
                    'ids': [1],
                    'model': 'reporte.permisionario.permiso',
                    }
                return {
                    'type':'ir.actions.report.xml',
                    'report_name':'tianguis__guadalajara.reporte_permisionario_permiso',
                    'datas':datas,
                    }
            elif self.report_tianguis == 'tarjetones_fotografia':
                datas = {}
                datas = {
                    'ids': [1],
                    'model': 'reporte.tarjetones.fotografia',
                    }
                return {
                    'type':'ir.actions.report.xml',
                    'report_name':'tianguis__guadalajara.reporte_tarjetones_fotografia',
                    'datas':datas,
                    }
        elif self.report_espacios and self.report_date_from and self.report_date_to:
            print 'aqui apenas vamoa a empezar perru'
    
    def reportToXlsx(self):
        if self.report_tianguis and self.report_date_from and self.report_date_to:
            if self.report_tianguis == 'informe_general':
                self.env.cr.execute("""select *from reporte_informe_general""")
                results = self.env.cr.dictfetchall()
                datas = {'ids':[]}
                datas['model'] = 'reporte.informe_general'
                datas['result'] = results
                return {'type': 'ir.actions.report.xml',
                    'report_name': 'tianguis__guadalajara.informe_general_report_xls.xlsx',
                    'datas': datas,
                    'name': 'INFORME GENERAL'
                }
            elif self.report_tianguis == 'giros_comerciales':
                self.env.cr.execute("""select *from reporte_giros_comerciales""")
                results = self.env.cr.dictfetchall()
                datas = {'ids':[]}
                datas['model'] = 'reporte.giros.comerciales'
                datas['result'] = results
                return {'type': 'ir.actions.report.xml',
                    'report_name': 'tianguis__guadalajara.giros_comerciales_report_xls.xlsx',
                    'datas': datas,
                    'name': 'LISTADO DE GIROS COMERCIALES EN GENERAL'
                }
            elif self.report_tianguis == 'puesto_permisionario':
                self.env.cr.execute("""select *from reporte_puestos_permisionario""")
                results = self.env.cr.dictfetchall()
                datas = {'ids':[]}
                datas['model'] = 'reporte.puestos.permisionario'
                datas['result'] = results
                return {'type': 'ir.actions.report.xml',
                    'report_name': 'tianguis__guadalajara.puestos_permisionario_report_xls.xlsx',
                    'datas': datas,
                    'name': 'REPORTE DE PUESTOS POR PERMISIONARIO'
                }
            elif self.report_tianguis == 'permisionario_permiso':
                self.env.cr.execute("""select *from reporte_permisionario_permiso""")
                results = self.env.cr.dictfetchall()
                datas = {'ids':[]}
                datas['model'] = 'reporte.permisinario.permiso'
                datas['result'] = results
                return {'type': 'ir.actions.report.xml',
                    'report_name': 'tianguis__guadalajara.permisionario_permiso_report_xls.xlsx',
                    'datas': datas,
                    'name': 'LISTADO DE PERMISIONARIOS CON PERMISO'
                }
            elif self.report_tianguis == 'tarjetones_fotografia':
                self.env.cr.execute("""select *from reporte_tarjetones_fotografia""")
                results = self.env.cr.dictfetchall()
                datas = {'ids':[]}
                datas['model'] = 'reporte.tarjetones.fotografia'
                datas['result'] = results
                return {'type': 'ir.actions.report.xml',
                    'report_name': 'tianguis__guadalajara.tarjetones_fotografia_report_xls.xlsx',
                    'datas': datas,
                    'name': 'ENTRGA DE TARJETONES CON FOTOGRAFIA'
                }
        elif self.report_espacios and self.report_date_from and self.report_date_to:
            print 'aqui apenas vamoa a empezar perru'
