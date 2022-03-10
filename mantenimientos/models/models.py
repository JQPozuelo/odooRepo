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

class mantenimiento(models.Model):
    _name = 'mantenimientos.mantenimiento'
    _description = 'Atributos del mantenimiento'

    TipoMantenimiento = fields.Char(string = 'Tipo de mantenimiento', required=True)
    Precio = fields.Integer(string = 'Precio del mantenimiento', required=True)
    Fecha = fields.date(string = 'Fecha de recepcion', required=True, default= fields.date.today())