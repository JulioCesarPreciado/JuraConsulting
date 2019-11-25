# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CUsuario(models.Model):
    _name = 'c_usuarios'

    chUsuario = fields.Char('Nombre del Usuario', required=1)
    vchPaterno = fields.Char('Apellido Paterno') 
    vchMaterno = fields.Char('Apellido Materno')
    vchNombre = fields.Char('Nombre', required=1)
    vchClave = fields.Char('Contraseña', required=1)
    tynArea = fields.Integer('Area', required=1) #Hacer un cátalogo de este campo
    tynNivel = fields.Integer('Nivel',required=1)
    vchConfiguracion = fields.Char('Configuración')
    estatus = fields.Selection([('A', 'Activo'), ('C', 'Cancelado')], string="Estatus", default='A')
    #nombre_completo = vchNombre + ' ' + vchPaterno + ' ' + vchMaterno


    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.estatus == 'A':
                name = record.vchNombre + ' ' + record.vchPaterno + ' ' + record.vchMaterno
                result.append((record.id, name))
        return result
    
    @api.model
    def create(self, vals):
        if vals.get('chUsuario', False):
            vals['chUsuario'] = vals.get('chUsuario', '').upper()
        if vals.get('vchPaterno', False):
            vals['vchPaterno'] = vals.get('vchPaterno', '').upper()
        if vals.get('vchMaterno', False):
            vals['vchMaterno'] = vals.get('vchMaterno', '').upper()
        if vals.get('vchNombre', False):
            vals['vchNombre'] = vals.get('vchNombre', '').upper()
        return super(CUsuario, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchDependendencia', False):
            vals['vchDependendencia'] = vals.get('vchDependendencia', '').upper()
        if vals.get('chPeriodo', False):
            vals['chPeriodo'] = vals.get('chPeriodo', '').upper()
        if vals.get('vchDirector', False):
            vals['vchDirector'] = vals.get('vchDirector', '').upper()
        if vals.get('vchLeyenda', False):
            vals['vchLeyenda'] = vals.get('vchLeyenda', '').upper()
        return super(CUsuario, self).write(vals)
    
    