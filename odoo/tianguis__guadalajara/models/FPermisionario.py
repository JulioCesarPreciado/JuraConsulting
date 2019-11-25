# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
class FPermisionario(models.Model):
    _name = 'c_permisionario'

    nombres = fields.Char(string="Nombre(s)", required=1)
    apellidoP = fields.Char(string="Apellido Paterno", required=1)
    apellidoM = fields.Char(string="Apellido Materno", required=1)
    domicilio = fields.Char(string="Domicilio", required=1)
    poblacion = fields.Many2one("c_poblacion", string="Población")
    colonia = fields.Many2one("c_colonias", string="Colonia")
    telefono = fields.Char("Teléfono")
    c_p = fields.Integer(
        "Código Postal", placeholder="Código Postal", required=1)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=1)
    sexo = fields.Selection(
        [('h', 'HOMBRE'), ('m', 'MUJER')], string='Género', required=1)
    imagen = fields.Binary("Fotografia")
    curp = fields.Char(string="CURP", required=1)
    rfc = fields.Char(string="RFC")
    escolaridad = fields.Selection(
        [('p', 'PRIMARIA'), ('S', 'SECUNDARIA'), ('B', 'BACHILLERATO'),
         ('L', 'LICENCIATURA'), ('P', 'POSGRADO')],
        string='Escolaridad')
    EstCiv = fields.Selection(
        [('S', 'SOLTERO(a)'), ('C', 'CASADO(a)')], string="Estado Civil")
    no_ext = fields.Char(string="No.Exterior", required=1)
    no_int = fields.Char(string="No.Interior")
    estatus = fields.Selection(
        [('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

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
        if vals.get('nombres', False):
            vals['nombres'] = vals.get('nombres', '').upper()
        if vals.get('apellidoP', False):
            vals['apellidoP'] = vals.get('apellidoP', '').upper()
        if vals.get('apellidoM', False):
            vals['apellidoM'] = vals.get('apellidoM', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        if vals.get('rfc', False):
            vals['rfc'] = vals.get('rfc', '').upper()
        if vals.get('domicilio', False):
            vals['domicilio'] = vals.get('domicilio', '').upper()
        return super(FPermisionario, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombres', False):
            vals['nombres'] = vals.get('nombres', '').upper()
        if vals.get('apellidoP', False):
            vals['apellidoP'] = vals.get('apellidoP', '').upper()
        if vals.get('apellidoM', False):
            vals['apellidoM'] = vals.get('apellidoM', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        if vals.get('rfc', False):
            vals['rfc'] = vals.get('rfc', '').upper()
        if vals.get('domicilio', False):
            vals['domicilio'] = vals.get('domicilio', '').upper()
        return super(FPermisionario, self).write(vals)
