# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
from odoo.exceptions import UserError

class Asistencia(models.Model):
    _name = 'asistencias'

    iPermisionar = fields.Many2one("permisionario", string="Permisionario")
    smlTianguis = fields.Many2one("c_tianguis", string="Tianguis")
    puesto = fields.Many2one('puestos', string="Puesto")
    smlAnno = fields.Integer("Año")
    vchSemanas = fields.Char("Semanas")
    tynEstado = fields.Boolean('Asistencia')

    @api.model
    def create(self, vals):
        if vals.get('vchSemanas', False):
            vals['vchSemanas'] = vals.get('vchSemanas', '').upper()
        return super(Asistencia, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('vchSemanas', False):
            vals['vchSemanas'] = vals.get('vchSemanas', '').upper()
        return super(Asistencia, self).write(vals)
    
    @api.multi
    def quitar_inasistencia(self):
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

