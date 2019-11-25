# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

class Configuracion(models.Model):
    _name = 'configuraciones'

    vchDependencia = fields.Char('Dependencia')
    chPeriodo = fields.Char('Periodo')
    vchDirector = fields.Char('Director')
    vchPresidente = fields.Char('Presidente')
    vchLeyenda = fields.Char('Leyenda')
    costo_m = fields.Float('Valor por metro', default=15)

    @api.model
    def create(self, vals):
        if vals.get('vchDependendencia', False):
            vals['vchDependendencia'] = vals.get('vchDependendencia', '').upper()
        if vals.get('chPeriodo', False):
            vals['chPeriodo'] = vals.get('chPeriodo', '').upper()
        if vals.get('vchDirector', False):
            vals['vchDirector'] = vals.get('vchDirector', '').upper()
        if vals.get('vchLeyenda', False):
            vals['vchLeyenda'] = vals.get('vchLeyenda', '').upper()
        return super(Configuracion, self).create(vals)

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
        return super(Configuracion, self).write(vals)