# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

# -----------catalogos pequeños---------------


class Pueblo(models.Model):
    _name = 'c_poblacion'

    c_poblaciones = fields.Char("Población")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = record.c_poblaciones
            result.append((record.id, name))
        return result
    @api.model
    def create(self, vals):
        if vals.get('c_poblaciones', False):
            vals['c_poblaciones'] = vals.get('c_poblaciones', '').upper()
        return super(Pueblo, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('c_poblaciones', False):
            vals['c_poblaciones'] = vals.get('c_poblaciones', '').upper()
        return super(Pueblo, self).write(vals)



class Municipio(models.Model):
    _name = 'c_municipios'

    NombreMunicipio = fields.Char('Municipio')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = record.NombreMunicipio
            result.append((record.id, name))
        return result


class Estado(models.Model):
    _name = 'c_estado'
    _rec_name = 'c_estados'

    c_estados = fields.Char("Estados")


class TbImpTarjeton(models.Model):
    _name = 'tb_imptarjeton'
    _rec_name = 'iFolio'

    iPermisionario = fields.Many2one(
        "permisionario", string="Permisionario")
    smltianguis = fields.Many2one("c_tianguis", string="Tianguis")
    iFolio = fields.Integer("Folio")


class TB_ValoresLista(models.Model):
    _name = "tb_valoreslista"

    smlValor = fields.Integer("ID")
    tynAgrupador = fields.Integer("Agrupador")
    vchDescripcion = fields.Char("Nombre del Recaudador")
    chCodigo = fields.Char("Codigo")
    vchValor = fields.Char("Valor")
    vchFamilia = fields.Char("Familia")


class CDependencias(models.Model):
    _name = "c_dependencias"

    nombre = fields.Char(string='Nombre')
