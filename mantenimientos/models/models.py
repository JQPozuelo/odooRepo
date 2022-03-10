# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mantenimientos(models.Model):
#     _name = 'mantenimientos.mantenimientos'
#     _description = 'mantenimientos.mantenimientos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

import string
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class descripcion(models.Model):
    _name = 'mantenimientos.descripcion'
    _description = 'Atributos del mantenimiento'

    TipoMantenimiento = fields.Char(string = 'Tipo de mantenimiento', requiered=True)
    Precio = fields.Integer(string = 'Precio del mantenimiento', requiered=True)
    Fecha = fields.Date(string = 'Fecha de recepcion', requiered=True, default= fields.date.today())