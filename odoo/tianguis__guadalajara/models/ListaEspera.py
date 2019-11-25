# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class ListaEspera(models.Model):
    _name = "lista_espera"

    smlTianguis = fields.Many2one("c_tianguis", string="Tianguis")
    iPermisionario = fields.Many2one("permisionario", string="Permisionario")
    smlGiroComercial = fields.Many2one(
        "c_giros_comerciales", string="Giro Comercial")
    vchFolioSemana = fields.Char("Folio Semana")
    tynPunto = fields.Integer("Punto")
    smlAnno = fields.Integer("Año")
    smlZonaTianguis = fields.Many2one(
        "c_zona_tianguis", string="Zona Tianguis")
    puesto = fields.Many2one('puestos', string="Puestos")

    @api.model
    def create(self, vals):
        if vals.get('vchFolioSemana', False):
            vals['vchFolioSemana'] = vals.get('vchFolioSemana', '').upper()
        return super(ListaEspera, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchFolioSemana', False):
            vals['vchFolioSemana'] = vals.get('vchFolioSemana', '').upper()
        return super(ListaEspera, self).write(vals)

    @api.multi
    def asignar_vacante(self):
        self.env.cr.execute(
            """UPDATE puestos SET "tynestatus" = 'A' WHERE "iPERMISIO" = %s AND id = %s""", (self.iPermisionario.id, self.puesto.id))
        return {
            'warning': {
                'title': 'Alerta',
                'message': 'El puesto ha sido asignado a la vacante!'}
        }
