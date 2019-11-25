# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CRecaudador(models.Model):
    _name = 'c_recaudador'

    paterno = fields.Char("Apellido Paterno", required=1)
    materno = fields.Char("Apellido Materno", required=1)
    nombre = fields.Char("Nombre", required=1)
    calle = fields.Char("Calle", required=1)
    no_ext = fields.Char(string="No.Exterior", required=1)
    no_int = fields.Char(string="No.Interior")
    colonia_id = fields.Many2one("c_colonias", string="Colonia")
    poblacion = fields.Many2one("c_poblacion", string="Población")
    cp = fields.Char("Código Postal")
    municipio = fields.Char("Municipio")
    sexo = fields.Selection(
        [('H', 'MASCULINO'), ('F', 'FEMENINO')], string="Género")
    dtNacimiento = fields.Date("Fecha de Nacimiento")
    telefono = fields.Char("Celular")
    estatus = fields.Selection(
        [('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')
    curp = fields.Char(string="CURP", required=1)
    contrasena = fields.Char(string="Contraseña")
    c_dependencia_id = fields.Many2one('c_dependencias', string='Direccion', default=2)
    tianguis_id = fields.Many2many('c_zona_tianguis', string="Tianguis")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if(record.estatus == 'A'):
                name = record.curp + ' - ' + record.nombre + \
                    ' ' + record.paterno + ' ' + record.materno
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('paterno', False):
            vals['paterno'] = vals.get('paterno', '').upper()
        if vals.get('materno', False):
            vals['materno'] = vals.get('materno', '').upper()
        if vals.get('calle', False):
            vals['calle'] = vals.get('calle', '').upper()
        if vals.get('no_ext', False):
            vals['no_ext'] = vals.get('no_ext', '').upper()
        if vals.get('no_int', False):
            vals['no_int'] = vals.get('no_int', '').upper()
        if vals.get('cp', False):
            vals['cp'] = vals.get('cp', '').upper()
        if vals.get('cp', False):
            vals['curp'] = vals.get('curp', '').upper()
        return super(CRecaudador, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('paterno', False):
            vals['paterno'] = vals.get('paterno', '').upper()
        if vals.get('materno', False):
            vals['materno'] = vals.get('materno', '').upper()
        if vals.get('calle', False):
            vals['calle'] = vals.get('calle', '').upper()
        if vals.get('no_ext', False):
            vals['no_ext'] = vals.get('no_ext', '').upper()
        if vals.get('no_int', False):
            vals['no_int'] = vals.get('no_int', '').upper()
        if vals.get('cp', False):
            vals['cp'] = vals.get('cp', '').upper()
        if vals.get('cp', False):
            vals['curp'] = vals.get('curp', '').upper()
        return super(CRecaudador, self).write(vals)
