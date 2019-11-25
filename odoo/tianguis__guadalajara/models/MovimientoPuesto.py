# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api

class MovimientoPuesto(models.Model):
    _name = 'movimientos_puestos'

    id = fields.Integer("iFolio")
    iCodMovimiento = fields.Integer("Movimiento")
    dtFechaMov = fields.Date("Fecha Movimiento")
    tynMovimiento = fields.Integer("iMovimiento")
    smlUsuario = fields.Integer("Usuario")
    iFolio = fields.Integer("Folio")
    iPermisionario = fields.Many2one("permisionario", string="Permisionario")
    tynDia = fields.Selection(
        [('L', 'Lunes'), ('M', 'Martes'), ('M', 'Mircolés'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sabado'),
         ('D', 'Domingo')], string="Día")
    smlTianguis = fields.Many2one("c_tianguis", string="Tianguis")
    iCodCalleInicio = fields.Char("Entre la Calle")
    iCodCalleFin = fields.Char("Y la Calle")
    smmInicia = fields.Float("Inicio")
    smmTermina = fields.Float("Termino")
    smlGiroComercial = fields.Many2one("c_giros_comerciales", string="Giro Comercial")
    tynSituacion = fields.Selection([('H', 'H. Ayuntamiento'), ('C', 'Cesión de Derechos'), ('A', 'Asignación')],
                                    string="Situación")
    vchComentario = fields.Char("Comentario")
    smlAdministrador = fields.Many2one("c_administrador", "Administrador")
    vchSuplente1 = fields.Char("1er Suplente")
    vchSuplente2 = fields.Char("2do Suplente")
    smlCuadra = fields.Char("Cuadra")
    smmDescuento = fields.Integer("Descuento")
    iZonaTianguis = fields.Many2one("c_zona_tianguis", string="Zona Tianguis")
    tynEstus = fields.Selection([('A', 'Activo'), ('C', 'Cancelado')], string="Estatus")
    tynVacante = fields.Boolean("Vacante")
    movimiento = fields.Char('Movimiento')
    fec = fields.Date('Fecha de creacion')