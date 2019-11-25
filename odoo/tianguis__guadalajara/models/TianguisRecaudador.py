import locale

from odoo import models, fields, api

class TianguisRecaudador(models.Model):
    _name = 'tianguis_recaudador'




    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nombre))
        return result

    