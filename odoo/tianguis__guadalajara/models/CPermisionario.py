# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class Permisionario(models.Model):
    _name = 'permisionario'
    _sql_constraints = [('curp', 'UNIQUE (curp)', 'La CURP ya existe en el sistema'),
                        ('rfc', 'UNIQUE (rfc)', 'La RFC ya existe en el sistema')]

    apellidoP = fields.Char(string="Apellido Paterno", required=1)
    apellidoM = fields.Char(string="Apellido Materno", required=1)
    nombres = fields.Char(string="Nombre(s)", required=1)
    domicilio = fields.Char(string="Domicilio", required=1)
    poblacion = fields.Many2one("c_poblacion", string="Población")
    colonia = fields.Many2one("c_colonias", string="Colonia")
    telefono = fields.Char("Teléfono")
    c_p = fields.Char("Código Postal", placeholder="Código Postal")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([(0, 'HOMBRE'), (1, 'MUJER')], string='Género')
    imagen = fields.Binary("Fotografia")
    padre = fields.Char("Padre")
    madre = fields.Char("Madre")
    conyugue = fields.Char("Conyugue")
    hijos = fields.Char("Hijos")
    curp = fields.Char(string="Curp")
    rfc = fields.Char(string="RFC")
    escolaridad = fields.Selection(
        [(48, 'PRIMARIA'), (50, 'SECUNDARIA'), (56, 'BACHILLERATO'),
         (57, 'LICENCIATURA'), (59, 'POSGRADO')],
        string='Escolaridad')
    EstCiv = fields.Selection(
        [(0, 'SOLTERO(A)'), (1, 'CASADO(A)')], string="Estado Civil")
    pagos_id = fields.One2many("pagos", "permisionario", string=".")
    permisos_id = fields.One2many("permisos", 'iPERMISIO', string=".")
    no_ext = fields.Char(string="No.Exterior")
    no_int = fields.Char(string="No.Interior")
    tynEstatus = fields.Selection(
        [(1, 'ACTIVO'), (2, 'CANCELADO')], string="Estatus",  default=1)
    saldo = fields.Float('Saldo Global')
    #---------------------- PUESTOS
    puestos_id = fields.One2many('puestos','iPERMISIO', string='Puestos id')
    puestos = fields.Many2one('puestos', string = 'Puestos')
    # -------------------- APERCIBIMIENTOS -------------------------------------
    apercibimientos_id = fields.One2many(
        "r_apercibimientos", "permisionario", string="Apercibimientos")
    # ---------------------- ESPACIOS ABIERTOS ------------------------------------------
    c_dependencia_id = fields.Many2one('c_dependencias', default=1)
    solicitud = fields.Integer(string='No. de Solicitud')
    # Suplente Número 1
    imagen1 = fields.Binary("Fotografia")
    apellidoP1 = fields.Char(string="Apellido Paterno 1")
    apellidoM1 = fields.Char(string="Apellido Materno 1")
    nombres1 = fields.Char(string="Nombre(s)")
    # Suplente Número 2
    imagen2 = fields.Binary("Fotografia")
    apellidoP2 = fields.Char(string="Apellido Paterno 2")
    apellidoM2 = fields.Char(string="Apellido Materno 2")
    nombres2 = fields.Char(string="Nombre(s)")
    # ---------------------------------- Puesto espacios abiertos
    puesto_espacios_a = fields.One2many(
        'puestos_espacios', 'iPERMISIO', string='Puestos')
    # ---------------------------------- DOCUMENTOS
    documentos_id = fields.One2many(
        'documentos', 'permisionario_id', string='Documentos')
    # ------------------------------ SELECCIÓN DE DESCUENTO
    descuento = fields.Boolean(string="Descuento")
    motivo_descuento = fields.One2many(
        "c_motivodescuento", 'permisionario', string="Motivo del Descuento")
    # -------------------------------- Puesto detalle
    puestos_detalles = fields.One2many('puesto_detalle','id_permisionario')

    def run_sql(self, qry):
        self._cr.execute(qry)
        _res = self._cr.fetchone()
        if(_res != None):
            return _res[0]
        return '-'

    @api.multi
    def name_get(self):
        result = []
        for permisionarios in self:
            name = '' + str(permisionarios.id) + '' + ' ' + permisionarios.apellidoP + ' ' + permisionarios.apellidoM + \
                   ' ' + permisionarios.nombres
            result.append((permisionarios.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('apellidoP', False):
            vals['apellidoP'] = vals.get('apellidoP', '').upper()
        if vals.get('apellidoM', False):
            vals['apellidoM'] = vals.get('apellidoM', '').upper()
        if vals.get('nombres', False):
            vals['nombres'] = vals.get('nombres', '').upper()
        if vals.get('apellidoP1', False):
            vals['apellidoP1'] = vals.get('apellidoP1', '').upper()
        if vals.get('apellidoM1', False):
            vals['apellidoM1'] = vals.get('apellidoM1', '').upper()
        if vals.get('nombres1', False):
            vals['nombres1'] = vals.get('nombres1', '').upper()
        if vals.get('apellidoP2', False):
            vals['apellidoP2'] = vals.get('apellidoP2', '').upper()
        if vals.get('apellidoM2', False):
            vals['apellidoM2'] = vals.get('apellidoM2', '').upper()
        if vals.get('nombres2', False):
            vals['nombres2'] = vals.get('nombres2', '').upper()
        if vals.get('domicilio', False):
            vals['domicilio'] = vals.get('domicilio', '').upper()
        if vals.get('padre', False):
            vals['padre'] = vals.get('padre', '').upper()
        if vals.get('madre', False):
            vals['madre'] = vals.get('madre', '').upper()
        if vals.get('conyugue', False):
            vals['conyugue'] = vals.get('conyugue', '').upper()
        if vals.get('hijos', False):
            vals['hijos'] = vals.get('hijos', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        if vals.get('rfc', False):
            vals['rfc'] = vals.get('rfc', '').upper()
        return super(Permisionario, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('apellidoP1', False):
            vals['apellidoP1'] = vals.get('apellidoP1', '').upper()
        if vals.get('apellidoM1', False):
            vals['apellidoM1'] = vals.get('apellidoM1', '').upper()
        if vals.get('nombres1', False):
            vals['nombres1'] = vals.get('nombres1', '').upper()
        if vals.get('apellidoP2', False):
            vals['apellidoP2'] = vals.get('apellidoP2', '').upper()
        if vals.get('apellidoM2', False):
            vals['apellidoM2'] = vals.get('apellidoM2', '').upper()
        if vals.get('nombres2', False):
            vals['nombres2'] = vals.get('nombres2', '').upper()
        if vals.get('apellidoP', False):
            vals['apellidoP'] = vals.get('apellidoP', '').upper()
        if vals.get('apellidoM', False):
            vals['apellidoM'] = vals.get('apellidoM', '').upper()
        if vals.get('nombres', False):
            vals['nombres'] = vals.get('nombres', '').upper()
        if vals.get('domicilio', False):
            vals['domicilio'] = vals.get('domicilio', '').upper()
        if vals.get('padre', False):
            vals['padre'] = vals.get('padre', '').upper()
        if vals.get('madre', False):
            vals['madre'] = vals.get('madre', '').upper()
        if vals.get('conyugue', False):
            vals['conyugue'] = vals.get('conyugue', '').upper()
        if vals.get('hijos', False):
            vals['hijos'] = vals.get('hijos', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        if vals.get('rfc', False):
            vals['rfc'] = vals.get('rfc', '').upper()
        return super(Permisionario, self).write(vals)

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(
            'tianguis__guadalajara.reporte_listado_general')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render('tianguis__guadalajara.reporte_listado_general', docargs)

    @api.multi
    def open_detalle(self):
        view_id_form = self.env['ir.ui.view'].search(
            [('name', '=', 'permisionario_pagos_wizard_view')])
        print view_id_form

    class PermisionarioPagosWizard(models.TransientModel):
        _name = 'permisionario.pagos.wizard'
