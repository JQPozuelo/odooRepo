# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class horarios(models.Model):
#     _name = 'horarios.horarios'
#     _description = 'horarios.horarios'

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

class horario(models.Model):
    _name = 'horarios.horario'
    _description = 'Define los atributos de un horario'
    
    #Relacion con tabla proyectos
    empleado_id = fields.One2many('proyectos.empleado', 'horario_id')

    #Atributos
    nombreHorario = fields.Char(string='Nombre horario', required=True)
    lunesEntrada = fields.Date(string='Hora entrada lunes')
    lunesSalida = fields.Date(string='Hora salida lunes')
    