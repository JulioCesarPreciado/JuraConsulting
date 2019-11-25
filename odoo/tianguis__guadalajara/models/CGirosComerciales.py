# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

class CGirosComerciales(models.Model):
    _name = 'c_giros_comerciales'
    
    vchGiroComercial = fields.Char (string = "Giro Comercial", required = 1)
    smlFamilia = fields.Many2one ("c_familiasgiros", string = "Familia")
    Descripcion = fields.Text('Descripcion')
    tynEstatus = fields.Selection([('A', 'ACTIVO'),('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if(record.tynEstatus == 'A'):
                result.append((record.id, record.vchGiroComercial))
        return result
    
    @api.model
    def create(self, vals):
        if vals.get('vchGiroComercial', False):
            vals['vchGiroComercial'] = vals.get('vchGiroComercial', '').upper()
        return super(CGirosComerciales, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchGiroComercial', False):
            vals['vchGiroComercial'] = vals.get('vchGiroComercial', '').upper()
        return super(CGirosComerciales, self).write(vals)