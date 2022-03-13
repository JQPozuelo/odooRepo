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
    #Atributos de la clase
    TipoMantenimiento = fields.Char(string='Tipo de mantenimiento', required=True)
    Precio = fields.Integer(string='Precio del mantenimiento', required=True)
    Apuntes = fields.Text(string='Notas de la reparacion', required=True, help='Apunta bien lo que haga falta')
    Fecha = fields.Date(string='Fecha de recepcion', required=True, default= fields.date.today())
    Prueba = fields.Integer('Prueba', compute='_getPr')

    #Prueba validacion
    @api.depends('Fecha')
    def _getPr(self):
        hoy = date.today()
        for descripcion in self:
            descripcion.Prueba = relativedelta(hoy, descripcion.Fecha).years


    #Relacion
    CocheSeleccionado = fields.Many2one('mantenimientos.coches', string='Coche')
    EmpresaS = fields.Many2one('proveedores.empresas', string='Distribuidor')
    #Validaciones y metodos
    def name_get(self):
        listaDescrip =  []
        for descripcion in self:
            listaDescrip.append((descripcion.id, descripcion.TipoMantenimiento))
        return listaDescrip


class coche(models.Model):
    _name = 'mantenimientos.coches'
    _description = 'Atributos del coche'

    #Atributos de la clase
    Modelo = fields.Char(string='Modelo del vehiculo', required=True)
    Anio = fields.Integer(string='Año de fabricacion', required=True)
    Motor = fields.Char(string='Tipo de motor', required=True)
    Combustible = fields.Selection(string='Combustible del vehiculo', selection=[('a', 'Gasolina'), ('b', 'Diesel')])
    NombrePropietario = fields.Char(string='Nombre del propietario', required=True)
    TelefonoPropietario = fields.Char(string='Telefono del propietario', required=True)
    
    #Validaciones y metodos
    def name_get(self):
        listaCoches =  []
        for coches in self:
            listaCoches.append((coches.id, coches.Modelo))
        return listaCoches

    @api.constrains('TelefonoPropietario')
    def _checkTelefono(self):
        for coches in self:
            if(len(coches.TelefonoPropietario) < 9):
                raise exceptions.ValidationError("El telefono no puede tener menos de 9 numeros")

    
   
