# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CSolicitante(models.Model):
    _name = 'c_solicitantes'
    _sql_constraints = [
        ('curp', 'UNIQUE (curp)', 'La CURP ya existe en el sistema')]

    nombre = fields.Char('Nombre')
    paterno = fields.Char(string='Paterno')
    materno = fields.Char(string='Materno')
    fca_nacimiento = fields.Date("Fecha de nacimiento")
    curp = fields.Char('CURP')
    telefono = fields.Char('Telefono')
    cp = fields.Integer('Código Postal')
    sexo = fields.Selection(
        [('H', 'HOMBRE'), ('M', 'MUJER')], string='Sexo')
    estatus = fields.Selection(
        [('A', 'ACEPTADO'), ('N', 'NO ACEPTADO'), ('C', 'CANCELADO')], string="Estatus",  default='N')

    # Pendiente geolocalización

    @api.multi
    def name_get(self):
        result = []
        for row in self:
            result.append((row.id, row.nombre))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('paterno', False):
            vals['paterno'] = vals.get('paterno', '').upper()
        if vals.get('materno', False):
            vals['materno'] = vals.get('materno', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        return super(CSolicitante, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('paterno', False):
            vals['paterno'] = vals.get('paterno', '').upper()
        if vals.get('materno', False):
            vals['materno'] = vals.get('materno', '').upper()
        if vals.get('curp', False):
            vals['curp'] = vals.get('curp', '').upper()
        return super(CSolicitante, self).write(vals)

    # Dimensiones
    medida_frente = fields.Float(string='Medidas de Frente')
    medida_fondo = fields.Float(string='Medidas de Fondo')

    # Horario
    hora_inicio = fields.Float(string='Hora Inicio')
    hora_fin = fields.Float(string='Hora Fin')
    hora_inicio2 = fields.Float(string='Hora Inicio2')
    hora_fin2 = fields.Float(string='Hora Fin2')
    mixto = fields.Boolean(string='Mixto')

    # Tipo y clase
    tipo = fields.Selection(string='Tipo', selection=[(
        'fijo', 'FIJO'), ('semifijo', 'SEMIFIJO'), ('ambulante', 'AMBULANTE')])
    clase = fields.Many2one('c_clases', string='Clase')

    # Dias de Venta
    lunes = fields.Boolean(string='Lunes')
    martes = fields.Boolean(string='Martes')
    miercoles = fields.Boolean(string='Miércoles')
    jueves = fields.Boolean(string='Jueves')
    viernes = fields.Boolean(string='Viernes')
    sabado = fields.Boolean(string='Sábado')
    domingo = fields.Boolean(string='Domingo')
    ocultar = fields.Boolean(string='Ocultar', default = False)

    # Familia y Giro
    familia = fields.Many2one('c_familiasgiros', string='Familia', placeholder='Seleccione una familia')
    giro = fields.Many2many(comodel_name='c_giros_comerciales',
                            string='Giro', placeholder='Seleccione un giro')

    # monto de movimiento
    monto = fields.Float(string='Monto de movimiento')

    @api.multi
    def asignar_permisionario(self):
        try:
            self.env.cr.execute(
                """INSERT INTO permisionario ("nombres", "apellidoP", "apellidoM", "domicilio", "no_ext","fecha_nacimiento", "curp", "telefono", "c_p", "sexo","solicitud","tynEstatus","c_dependencia_id")
                VALUES (%s,%s,%s,'','',%s,%s,%s,%s,%s,%s,'A',4); UPDATE c_solicitantes SET estatus = 'A' WHERE id = %s ;
                INSERT INTO puestos_espacios ("tipo","clase","hora_fin","hora_fin2", "hora_inicio","hora_inicio2","mixto","medidas_fondo","medidas_frente",
                "lunes","martes","miercoles","jueves","viernes","sabado","domingo","solicitud") VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                UPDATE puestos_espacios SET "iPERMISIO" = p.id FROM(SELECT id FROM permisionario WHERE solicitud = %s) AS p
                WHERE puestos_espacios.solicitud = %s;""", (self.nombre, self.paterno, self.materno, self.fca_nacimiento, self.curp, self.telefono, self.cp, self.sexo, self.id, self.id,
                self.tipo, self.clase.id, self.hora_fin, self.hora_fin2,
                self.hora_inicio, self.hora_inicio2, self.mixto, self.medida_fondo, self.medida_frente,
                self.lunes, self.martes, self.miercoles, self.jueves, self.viernes, self.sabado, self.domingo, self.id, self.id, self.id))
            self.ocultar = True
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict({})
            context['message'] = "Solicitud Aceptada"
            return {
                'name':'Exito',
                'type':'ir.actions.act_window',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'sh.message.wizard',
                'views':[(view.id,'form')],
                'view_id':view.id,
                'target':'new',
                'context':context,
            }
        except Exception ,ex:
            raise UserError("Error al asignar el solicitante: " + str(ex))


class Clase(models.Model):
    _name = 'c_clases'

    Descripcion = fields.Text(string='Descripción')
    nombre = fields.Char('Nombre')
    FechaInicio = fields.Date(string='Fecha de Inicio')
    FechaTermino = fields.Date(string='Fecha de Termino')
    Comentarios = fields.Text(string='Comentarios')

    @api.multi
    def name_get(self):
        result = []
        for row in self:
            result.append((row.id, row.nombre))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('Descripcion', False):
            vals['Descripcion'] = vals.get('Descripcion', '').upper()
        if vals.get('Comentarios', False):
            vals['Comentarios'] = vals.get('Comentarios', '').upper()
        return super(Clase, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre', False):
            vals['nombre'] = vals.get('nombre', '').upper()
        if vals.get('Descripcion', False):
            vals['Descripcion'] = vals.get('Descripcion', '').upper()
        if vals.get('Comentarios', False):
            vals['Comentarios'] = vals.get('Comentarios', '').upper()
        return super(Clase, self).write(vals)

    
    
    
    
    

