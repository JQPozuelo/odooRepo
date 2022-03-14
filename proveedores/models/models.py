# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proveedores(models.Model):
#     _name = 'proveedores.proveedores'
#     _description = 'proveedores.proveedores'

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

class empresas(models.Model):
    _name = 'proveedores.empresas'
    _description = 'Atributos de las empresas'

    #Atributos de la clase
    NIFEmpresa = fields.Char(string='NIF de la empresa', required=True)
    NombreEmpresa = fields.Char(string='Nombre de la empresa', required=True)
    Localizacion = fields.Char(string='Localidad de la empresa', required=True)
    Facturacion = fields.Integer(string='Facturacion mensual', required=True)

    #Relaciones
    materiales_id = fields.Many2many('proveedores.materiales', string='Materiales a pedir')

    #Validaciones y metodos
    def name_get(self):
        listaEmpresas =  []
        for empresas in self:
            listaEmpresas.append((empresas.id, empresas.NombreEmpresa))
        return listaEmpresas
    
    @api.constrains('NIFEmpresa')
    def _checkNIF(self):
        for empresas in self:
            if(len(empresas.NIFEmpresa) > 5):
                raise exceptions.ValidationError("El NIF no puede tener mas de 5 numeros")

class materiales(models.Model):
    _name = 'proveedores.materiales'
    _description = 'Atributos de los materiales'

    #Atributos de la clase
    IdPieza = fields.Char(string='Referencia de la pieza', required=True)
    NombrePieza = fields.Char(string='Nombre de la pieza', required=True)
    CostePieza = fields.Integer(string='Coste de la pieza', required=True)

    #Relacion
    empresaSeleccionada = fields.Many2one('proveedores.empresas', string='Empresa')
    
    #Validaciones y metodos
    def name_get(self):
        listaMateriales =  []
        for materiales in self:
            listaMateriales.append((materiales.id, materiales.NombrePieza))
        return listaMateriales