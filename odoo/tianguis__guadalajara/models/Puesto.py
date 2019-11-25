# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Puesto(models.Model):
    _name = 'puestos'

    #_sql_constraints = [ ('unique_product', 'UNIQUE(iPERMISIO, smlTIANGUIS)', 'Cannot Use one tracker twice!\nPlease, select a different product')	]
    
    iPERMISIO = fields.Many2one('permisionario', string='Permisionario')
    tynDia = fields.Selection([(0, 'LUNES'), (1, 'MARTES'), (2, 'MIERCOLES'), ( 3, 'JUEVES'), (4, 'VIERNES'), (5, 'SABADO'), (6, 'DOMINGO')], string="Día")
    smlTIANGUIS = fields.Many2one("c_tianguis", string="Tianguis")
    vchCALLE1 = fields.Many2one("c_calles", string="Calle 1")
    vchCALLE1_copy = fields.Integer()  # Copias para guardar
    vchCALLE2 = fields.Many2one("c_calles", string="Calle 2")
    vchCALLE2_copy = fields.Integer()  # Copias para guardar
    smmINICIA = fields.Float("Inicio")
    smmTERMINA = fields.Float("Termino")
    smmLONGITUD = fields.Float("Longitud")
    smmLONGITUD_copy = fields.Float()  # Copias para guardar
    smlGIRO1 = fields.Many2one("c_giros_comerciales", string="Giro Comercial")
    tynSITUACION = fields.Selection( [(0, 'H. AYUNTAMIENTO'), (1, 'CESIÓN DE DERECHOS'), (2, 'ASIGNACIÓN')], string="Situación")
    vchCOMENTARIO = fields.Text('Comentario')
    smlAdministrador = fields.Many2one("c_administrador", "Administrador")
    vchSUPLENTE1 = fields.Char("1er Suplente")
    vchSUPLENTE2 = fields.Char("2do Suplente")
    smlCUADRA = fields.Char("Ubicacion")
    smlCUADRA_copy = fields.Char()  # Copias para guardar
    tynestatus = fields.Selection([(0,'FIJO'), (1, 'ROLERO'), (2, 'VACANTE'), (3, 'ESPACIO NEGRO'), (4,'PROCESO DE REVOCACION')], string="Estatus")
    iDescuento = fields.Integer("Descuento", default=0)
    imovimiento = fields.Integer("Movimiento")
    iZonaT = fields.Many2one("c_zona_tianguis", string="Zona Tianguis")
    tynMovimientoDescuento = fields.Integer("iMovimiento")
    iTarjeton = fields.Integer('Folio tarjeton')
    iTarjeton_copy = fields.Integer('Folio tarjeton') # Copias para guardar
    tynVacante = fields.Boolean('Vacante')
    valor = fields.Float('Valor')
    valor_copy = fields.Float()  # Copias para guardar
    puntos = fields.Integer(string='Puntos')
    saldo_puesto = fields.Float(string='Saldo del Puesto')

    def run_sql(self, qry):
        self._cr.execute(qry)
        _res = self._cr.fetchone()
        return _res[0]

    @api.onchange('smmINICIA', 'smmTERMINA')
    def onchange_longitud(self):
        if self.smmINICIA or self.smmTERMINA:
            if self.smmINICIA < self.smmTERMINA:
                qry = """ SELECT c_calles."smlLongitud" FROM c_zona_tianguis
                    JOIN c_calles_tianguis ON c_zona_tianguis."CallePrincipal" = c_calles_tianguis.id
                    JOIN c_calles ON c_calles_tianguis."iCallesTianguis" = c_calles.id
                    WHERE c_zona_tianguis.id = """ + str(self.iZonaT.id) + """;"""
                self._cr.execute(qry)
                _res = self._cr.fetchall()
                for longitud in _res:
                    if self.smmINICIA < longitud[0]:
                        resta = self.smmTERMINA - self.smmINICIA
                        resta_calle = int(longitud[0]) - self.smmINICIA
                        if(resta <= resta_calle):
                            self.smmLONGITUD = self.smmTERMINA - self.smmINICIA
                            self.smmLONGITUD_copy = self.smmTERMINA - self.smmINICIA
                            self.valor = self.smmLONGITUD * 9
                            self.valor_copy = self.smmLONGITUD * 9
                        else:
                            view = self.env.ref('sh_message.sh_message_wizard')
                            view_id = view and view.id or False
                            context = dict({})
                            context['message'] = "El puesto excede la longitud de la calle"
                            return {
                                'name':'Error',
                                'type':'ir.actions.act_window',
                                'view_type':'form',
                                'view_mode':'form',
                                'res_model':'sh.message.wizard',
                                'views':[(view.id,'form')],
                                'view_id':view.id,
                                'target':'new',
                                'context':context,
                            }
                    else:
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict({})
                        context['message'] = "Inicia es mayor que la longitud de la calle"
                        return {
                            'name':'Error',
                            'type':'ir.actions.act_window',
                            'view_type':'form',
                            'view_mode':'form',
                            'res_model':'sh.message.wizard',
                            'views':[(view.id,'form')],
                            'view_id':view.id,
                            'target':'new',
                            'context':context,
                        }
            else:
                self.smmLONGITUD = 0
                self.smmLONGITUD_copy = 0

    @api.onchange('iZonaT')
    def calle_principal(self):
        if self.iZonaT:
            qry = """ SELECT c_calles."vchCalle" FROM c_calles_tianguis JOIN c_calles ON c_calles.id = c_calles_tianguis."iCallesTianguis"
                JOIN c_zona_tianguis ON c_zona_tianguis."CallePrincipal" = c_calles_tianguis.id  WHERE c_zona_tianguis.id = """ + str(self.iZonaT.id) + """;"""
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.smlCUADRA = str(_res[0])
            self.smlCUADRA_copy = str(_res[0])

    @api.onchange('iZonaT')
    def calle_cruce_inicial(self):
        if self.iZonaT:
            qry = """ SELECT c_calles.id FROM c_zona_tianguis
            JOIN c_calles ON c_calles.id = c_zona_tianguis."CalleCruceIni"
            WHERE c_zona_tianguis.id = """ + \
                str(self.iZonaT.id) + """;"""
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.vchCALLE1 = int(_res[0])
            self.vchCALLE1_copy = int(_res[0])

    @api.onchange('iZonaT')
    def calle_cruce_final(self):
        if self.iZonaT:
            qry = """ SELECT c_calles.id FROM c_zona_tianguis
            JOIN c_calles ON c_calles.id = c_zona_tianguis."CalleCruceFin"
            WHERE c_zona_tianguis.id = """ + \
                str(self.iZonaT.id)
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.vchCALLE2 = int(_res[0])
            self.vchCALLE2_copy = int(_res[0])

    @api.onchange('tynVacante')
    def onchange_vacante(self):
        self.iPERMISIO = 1
        self.tynestatus = 'V'
        self.valor = 0
        self.tynSITUACION = 'H'
        self.vchSUPLENTE1 = None
        self.vchSUPLENTE2 = None
        self.smlGIRO1 = None
        self.vchCOMENTARIO = None

    @api.multi
    def name_get(self):
        result = []
        for puesto in self:
            name = str(puesto.id) + '' + ' ' + str(puesto.smlTIANGUIS.nombre) + ' Linea: ' + \
                str(puesto.iZonaT.chZonaTianguis) + ' Zona: ' + \
                str(puesto.iZonaT.smlZonaTianguis)
            result.append((puesto.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('vchCOMENTARIO', False):
            vals['vchCOMENTARIO'] = vals.get('vchCOMENTARIO', '').upper()
        if vals.get('vchSUPLENTE1', False):
            vals['vchSUPLENTE1'] = vals.get('vchSUPLENTE1', '').upper()
        if vals.get('vchSUPLENTE2', False):
            vals['vchSUPLENTE2'] = vals.get('vchSUPLENTE2', '').upper()
        if 'smlCUADRA_copy' in vals:
            vals.update({'smlCUADRA': vals.get('smlCUADRA_copy')})
        if 'vchCALLE1_copy' in vals:
            vals.update({'vchCALLE1': vals.get('vchCALLE1_copy')})
        if 'vchCALLE2_copy' in vals:
            vals.update({'vchCALLE2': vals.get('vchCALLE2_copy')})
        if 'smmLONGITUD_copy' in vals:
            vals.update({'smmLONGITUD': vals.get('smmLONGITUD_copy')})
        if 'valor_copy' in vals:
            vals.update({'valor': vals.get('valor_copy')})
        if 'iTarjeton_copy' in vals:
            vals.update({'iTarjeton': vals.get('iTarjeton_copy')})

        return super(Puesto, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchCOMENTARIO', False):
            vals['vchCOMENTARIO'] = vals.get('vchCOMENTARIO', '').upper()
        if vals.get('vchSUPLENTE1', False):
            vals['vchSUPLENTE1'] = vals.get('vchSUPLENTE1', '').upper()
        if vals.get('vchSUPLENTE2', False):
            vals['vchSUPLENTE2'] = vals.get('vchSUPLENTE2', '').upper()
        if 'smlCUADRA_copy' in vals:
            vals.update({'smlCUADRA': vals.get('smlCUADRA_copy')})
        if 'vchCALLE1_copy' in vals:
            vals.update({'vchCALLE1': vals.get('vchCALLE1_copy')})
        if 'vchCALLE2_copy' in vals:
            vals.update({'vchCALLE2': vals.get('vchCALLE2_copy')})
        if 'smmLONGITUD_copy' in vals:
            vals.update({'smmLONGITUD': vals.get('smmLONGITUD_copy')})
        if 'valor_copy' in vals:
            vals.update({'valor': vals.get('valor_copy')})
        if 'iTarjeton_copy' in vals:
            vals.update({'iTarjeton': vals.get('iTarjeton_copy')})
        return super(Puesto, self).write(vals)

    @api.onchange('tynDia')
    def cambio_tianguis(self):
        if self.tynDia:
            self.smlTIANGUIS = None

    @api.onchange('smlTIANGUIS')
    def cambio_linea(self):
        if self.smlTIANGUIS:
            self.iZonaT = None

    @api.onchange('iPERMISIO')
    def cambio_tarjeton(self):
        if self.iPERMISIO:
            qry = """SELECT permisionario.id FROM permisionario
            INNER JOIN puestos on permisionario.id = puestos."iPERMISIO"
            WHERE permisionario.id = """ + \
                str(self.iPERMISIO.id)
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.iTarjeton = int(_res[0])
            self.iTarjeton_copy = int(_res[0]) 

    @api.constrains('email')
    def validar_puesto(self):
        for record in self:
            qry = """SELECT * FROM puestos WHERE "iPERMISIO" = """ + str(record.iPERMISIO.id) + """ AND smlTIANGUIS """ + str(record.smlTIANGUIS.id)
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            if(_res != None):
                raise ValidationError("Your record is too old:")

    