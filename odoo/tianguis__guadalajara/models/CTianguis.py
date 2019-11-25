# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CTianguis(models.Model):
    _name = 'c_tianguis'
    
    nombre = fields.Char("Tianguis")
    calle_ubicacion_id = fields.Text(string="Ubicación")
    colonia_id = fields.Many2one("c_colonias", string="Colonia")
    estatus = fields.Selection(
        [('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')
    tynDia = fields.Selection([(1, 'LUNES'), (2, 'MARTES'), (3, 'MIERCOLES'), (
        4, 'JUEVES'), (5, 'VIERNES'), (6, 'SABADO'), (7, 'DOMINGO')], string="Día")
    fecha_reporte = fields.Date(string='Fecha de reporte')

    def run_sql(self, fecha, nombre):
        qry = """ 
              SELECT 
              CONCAT(b.nombres,' ',b."apellidoP",' ',b."apellidoM") AS permisionario, 
              CONCAT(d."smlZonaTianguis",d."chZonaTianguis") AS puesto,
              c."valor",a."cargo",a."abono",
              CASE WHEN b."descuento" = false THEN 'SIN DESCUENTO' ELSE 'CON DESCUENTO: 50%' END AS descuento,
              CASE WHEN c."tynestatus" = 'F' THEN 'FIJO' ELSE 'ROLERO' END AS estatus
              FROM pagos a JOIN permisionario b ON  b.id = a."permisionario"
              JOIN puestos c ON c.id = a."puesto" JOIN c_zona_tianguis d ON d.id = c."iZonaT"
              JOIN c_tianguis ON c_tianguis.id = c."smlTIANGUIS"
              WHERE c_tianguis.nombre = '""" + str(nombre) + """' AND Date(a."date_action") = '""" + str(fecha) + "'"
        self._cr.execute(qry)
        _res = self._cr.fetchall()
        if(_res != None):
            return _res
        return '-'
    
    def sum_valor(self,fecha,nombre):
        qry = """ 
              SELECT 
              SUM(valor) AS valorTotal,
              SUM(cargo) AS cargoTotal,
              SUM(abono) AS abonoTotal,
              SUM(CASE WHEN descuento  = true THEN 1 ELSE 0 END) as conDescuento,
              SUM(CASE WHEN descuento  = false THEN 1 ELSE 0 END) as sinDescuento,
              SUM(CASE WHEN c."tynestatus" = 'F'THEN 1 ELSE 0 END) as conDescuento,
              SUM(CASE WHEN c."tynestatus" = 'R' THEN 1 ELSE 0 END) as sinDescuento
              FROM pagos a JOIN permisionario b ON  b.id = a."permisionario"
              JOIN puestos c ON c.id = a."puesto" JOIN c_zona_tianguis d ON d.id = c."iZonaT"
              JOIN c_tianguis ON c_tianguis.id = c."smlTIANGUIS"
              WHERE c_tianguis.nombre = '""" + str(nombre) + """' AND Date(a."date_action") = '""" + str(fecha) + "'"
        self._cr.execute(qry)
        _res = self._cr.fetchone()
        if(_res != None):
            return _res
        return '-'
        

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.estatus == 'A':
                name = record.nombre
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('ubicacion', False):
            vals['ubicacion'] = vals.get('ubicacion', '').upper()
        return super(CTianguis, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('ubicacion', False):
            vals['ubicacion'] = vals.get('ubicacion', '').upper()
        return super(CTianguis, self).write(vals)

    @api.multi
    def generate_report(self):
        return self.env.ref('tianguis__guadalajara.report_pagos_tianguis').report_action(self)