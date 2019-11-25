# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api


class PuestoEspacios(models.Model):
    _name = 'puestos_espacios'

    # Datos de la solicitud
    solicitud = fields.Integer("No. Solicitud")
    FechaRec = fields.Date("Fecha de recibido")
    iPERMISIO = fields.Many2one('permisionario', string='Permisionario')

    # Ubicación

    # Dias de Venta
    lunes = fields.Boolean(string='Lunes')
    martes = fields.Boolean(string='Martes')
    miercoles = fields.Boolean(string='Miércoles')
    jueves = fields.Boolean(string='Jueves')
    viernes = fields.Boolean(string='Viernes')
    sabado = fields.Boolean(string='Sábado')
    domingo = fields.Boolean(string='Domingo')

    # Horario
    hora_inicio = fields.Float(string='Hora Inicio')
    hora_fin = fields.Float(string='Hora Fin')
    hora_inicio2 = fields.Float(string='Hora Inicio2')
    hora_fin2 = fields.Float(string='Hora Fin2')
    mixto = fields.Boolean(string='Mixto')
    
    # Datos del puesto    
    medidas_frente = fields.Float('Medidas de Frente')
    medidas_fondo = fields.Float('Medidas de Fondo')

    # Tipo y clase
    tipo = fields.Selection(string='Tipo', selection=[(
        'fijo', 'FIJO'), ('semifijo', 'SEMIFIJO'), ('ambulante', 'AMBULANTE')])
    clase = fields.Many2one('c_clases', string='Clase')

    # Familia y Giro
    familia = fields.Many2one('c_familiasgiros',string='Familia', placeholder='Seleccione una familia')
    giro = fields.Many2many(comodel_name='c_giros_comerciales',string='Giro', placeholder='Seleccione un giro')

    # monto de movimiento
    monto = fields.Float(string='Monto de movimiento')
    valor = fields.Float(string='Valor')
    

    # Supervisor
    supervisor = fields.Integer(string='Supervisor')

    #Fechas
    fca_asignacion = fields.Date("Fecha de Asignación")
    
