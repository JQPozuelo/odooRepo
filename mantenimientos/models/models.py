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

    TipoMantenimiento = fields.Char(string='Tipo de mantenimiento', requiered=True)
    Precio = fields.Integer(string='Precio del mantenimiento', requiered=True)
    Apuntes = fields.Text(string='Notas de la reparacion', requiered=True, help='Apunta bien lo que haga falta')
    Fecha = fields.Date(string='Fecha de recepcion', requiered=True, default= fields.date.today())

    #Relacion
    CocheSeleccionado = fields.Many2one('mantenimientos.coches', string='Coche')

    def name_get(self):
        listaDescrip =  []
        for descripcion in self:
            listaDescrip.append((descripcion.id, descripcion.TipoMantenimiento))
        return listaDescrip


class coche(models.Model):
    _name = 'mantenimientos.coches'
    _description = 'Atributos del coche'

    Modelo = fields.Char(string='Modelo del vehiculo', requiered=True)
    Anio = fields.Integer(string='Año de fabricacion', requiered=True)
    Motor = fields.Char(string='Tipo de motor', requiered=True)
    Combustible = fields.Selection(string='Combustible del vehiculo', selection=[('a', 'Gasolina'), ('b', 'Diesel')])
    NombrePropietario = fields.Char(string='Nombre del propietario', requiered=True)
    TelefonoPropietario = fields.Char(string='Telefono del propietario', requiered=True)
    
    @api.constrains('TelefonoPropietario')
    def _checkTelefono(self):
        for coches in self:
            if(len(coches.TelefonoPropietario) < 9):
                raise exceptions.ValidationError("El telefono no puede tener menos de 9 numeros")
