
# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class CZonaTianguis(models.Model):
    _name = 'c_zona_tianguis'
    # _rec_name = 'iZonaTianguis'

    smlTianguis = fields.Many2one("c_tianguis", string='Tianguis')
    chZonaTianguis = fields.Char("Lineas")
    smlZonaTianguis = fields.Integer('Zona')
    CallePrincipal = fields.Many2one("c_calles_tianguis", string="Calle principal")
    CalleCruceIni = fields.Many2one("c_calles", string="Calle Cruce Inicial")
    CalleCruceIni_copy = fields.Many2one("c_calles", string="Calle Cruce Inicial") # Copia para guardar
    CalleCruceFin = fields.Many2one("c_calles", string="Calle Cruce Final")
    CalleCruceFin_copy = fields.Many2one("c_calles", string="Calle Cruce Final")
    estatus = fields.Selection(
        [('A', 'ACTIVO'), ('C', 'CANCELADO')], string="Estatus",  default='A')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if (record.estatus == 'A'):
                name =  'Zona: ' + str(record.smlZonaTianguis) + ' Linea: ' + record.chZonaTianguis
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('chZonaTianguis', False):
            vals['chZonaTianguis'] = vals.get('chZonaTianguis', '').upper()
        if 'CalleCruceIni_copy' in vals:
            vals.update({'CalleCruceIni': vals.get('CalleCruceIni_copy')})
        if 'CalleCruceFin_copy' in vals:
            vals.update({'CalleCruceFin': vals.get('CalleCruceFin_copy')})
        return super(CZonaTianguis, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('chZonaTianguis', False):
            vals['chZonaTianguis'] = vals.get('chZonaTianguis', '').upper()
        if 'CalleCruceIni_copy' in vals:
            vals.update({'CalleCruceIni': vals.get('CalleCruceIni_copy')})
        if 'CalleCruceFin_copy' in vals:
            vals.update({'CalleCruceFin': vals.get('CalleCruceFin_copy')})
        return super(CZonaTianguis, self).write(vals)
    
    @api.onchange('CallePrincipal')
    def calle_cruce_inicial(self):
        if self.CallePrincipal:
            qry = """ SELECT c_calles."iCalleInicio" FROM c_calles_tianguis
                JOIN c_calles ON c_calles.id = c_calles_tianguis."iCallesTianguis"
                WHERE c_calles_tianguis.id = """ + \
                str(self.CallePrincipal.id) + """;"""
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.CalleCruceIni = int(_res[0])
            self.CalleCruceIni_copy = int(_res[0])

    @api.onchange('CallePrincipal')
    def calle_cruce_final(self):
        if self.CallePrincipal:
            qry = """ SELECT c_calles."iCalleFinal" FROM c_calles_tianguis
                JOIN c_calles ON c_calles.id = c_calles_tianguis."iCallesTianguis"
                WHERE c_calles_tianguis.id = """ + \
                str(self.CallePrincipal.id)
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.CalleCruceFin = int(_res[0])
            self.CalleCruceFin_copy = int(_res[0])

    @api.onchange('smlTianguis')
    def clean_fields(self):
        self.CalleCruceIni = None
        self.CallePrincipal = None
        self.CalleCruceFin = None


