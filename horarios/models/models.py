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
from datetime import datetime
from dateutil.relativedelta import *

class horario(models.Model):
    _name = 'horarios.horario'
    _description = 'Define los atributos de un horario'
    
    #Relacion con tabla proyectos
    empleado_id = fields.One2many('proyectos.empleado', 'horario_id')

    #Atributos
    nombreHorario = fields.Char(string='Nombre horario', required=True)

    lunesEntrada = fields.Selection(string='Hora entrada lunes', selection='_get_valid_hours', default='8.5')
    lunesSalida = fields.Selection(string='Hora salida lunes', selection='_get_valid_hours', default='8.5')

    martesEntrada = fields.Selection(string='Hora entrada martes', selection='_get_valid_hours', default='8.5')
    martesSalida = fields.Selection(string='Hora salida martes', selection='_get_valid_hours', default='8.5')

    miercolesEntrada = fields.Selection(string='Hora entrada miercoles', selection='_get_valid_hours', default='8.5')
    miercolesSalida = fields.Selection(string='Hora salida miercoles', selection='_get_valid_hours', default='8.5')

    juevesEntrada = fields.Selection(string='Hora entrada jueves', selection='_get_valid_hours', default='8.5')
    juevesSalida = fields.Selection(string='Hora salida jueves', selection='_get_valid_hours', default='8.5')

    viernesEntrada = fields.Selection(string='Hora entrada viernes', selection='_get_valid_hours', default='8.5')
    viernesSalida = fields.Selection(string='Hora salida viernes', selection='_get_valid_hours', default='8.5')

    @api.model
    def _get_valid_hours(self):
        selection = [
            ('8', '8:00'),   ('8.5', '8:30'),
            ('9', '9:00'),   ('9.5', '9:30'),
            ('10', '10:00'), ('10.5', '10:30'),
            ('11', '11:00'), ('11.5', '11:30'),
            ('12', '12:00'), ('12.5', '12:30'),
            ('13', '13:00'), ('13.5', '13:30'),
            ('14', '14:00'), ('14.5', '14:30'),
            ('15', '15:00'), ('15.5', '15:30'),
            ('16', '16:00'), ('16.5', '16:30'),
            ('17', '17:00'), ('17.5', '17:30'),
            ('18', '18:00')
        ]
        return selection

    @api.constrains('lunesEntrada')
    def change_data_field(self):
        he = float(self.lunesEntrada)
        hs = float(self.lunesSalida)
        if(he > hs):
            raise exceptions.ValidationError("La hora de salida del Lunes tiene que ser mayor que la de entrada")

    