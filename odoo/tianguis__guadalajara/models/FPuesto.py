# -*- coding: utf-8 -*-
import locale

from odoo import models, fields, api
class Puesto(models.Model):
    _name = 'f_puestos'
    permisionario = fields.Many2one('c_permisionario',string = "Permisionario")
    festividad = fields.Many2one('c_festividades' ,string = "Festividad")
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    juego = fields.Boolean(string = "Juego Mecánico")
    comercio = fields.Boolean(string = "Comercio")
    largo = fields.Float(string = "Largo")
    ancho = fields.Float(string = "Ancho")  
    costo = fields.Float(string = "Costo")
    comentarios = fields.Text(string = "Comentarios")
    imagen = fields.Binary("Fotografia")
    estatus = fields.Selection([('A', 'Activo'), ('C', 'Cancelado')], string="Estatus",  default='A') 
    juegos_mecanicos = fields.Many2one ("c_juegos_mecanicos" , string = "Juego")
    giros = fields.Many2one("c_comercio_festividades", string = "Giro Comercial")
    lugar = fields.Many2one('lugar_festividad', string = "Lugar del Puesto")
    nombre_dictamen = fields.Char("Nombre del archivo")
    dictamen = fields.Binary(string='Documento')
    tiene_dictamen = fields.Boolean(string='Tiene dictamen?')


    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if(record.estatus == 'A'):
                name = str(record.id) + '' + ' ' + str(record.permisionario.nombres) + ''+ \
                str(record.festividad) 
                result.append((record.id, name))
        return result

    @api.model
    def create(self, vals):
        if vals.get('nombre_dictamen', False):
            vals['nombre_dictamen'] = vals.get('nombre_dictamen', '').upper()
        if vals.get('comentarios', False):
            vals['comentarios'] = vals.get('comentarios', '').upper()
        return super(Puesto, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('nombre_dictamen', False):
            vals['nombre_dictamen'] = vals.get('nombre_dictamen', '').upper()
        if vals.get('comentarios', False):
            vals['comentarios'] = vals.get('comentarios', '').upper()
        return super(Puesto, self).write(vals)

    @api.onchange('festividad')
    def inicio(self):
        if self.festividad:
            qry = """ SELECT c_festividades."fecha_inicio" FROM c_festividades 
            INNER JOIN f_puestos ON c_festividades.id = f_puestos.festividad
            WHERE c_festividades."nombre" = '""" + str(self.festividad.nombre) + "'"
            self._cr.execute(qry)
            _res = self._cr.fetchall()
            self.fecha_inicio = str(_res[0])

        
    @api.onchange('festividad')
    def fin(self):
        if self.festividad:
            qry = """ SELECT c_festividades."fecha_fin" FROM c_festividades 
            INNER JOIN f_puestos ON c_festividades.id = f_puestos.festividad
            WHERE c_festividades."nombre" = '""" + str(self.festividad.nombre) + "'"
            self._cr.execute(qry)
            _res = self._cr.fetchone()
            self.fecha_fin = str(_res[0])
            
            