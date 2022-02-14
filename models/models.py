# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

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

class departamento(models.Model):
    _name = 'proyectos.departamento'
    _description = 'Define los atributos de un departamento'
    
    nombreDepartamento= fields.Char(string='Nombre departamento', required=True)
    
    #Comentario de prueba
    empleado_id = fields.One2many('proyectos.empleado','departamento_id' ,string='Departamento')

class empleado(models.Model):
    _name = 'proyectos.empleado'
    _description = 'Atributos para un empleado'
    #atributos
    dniEmpleado = fields.Char(string='DNI', requiered=True)
    nombreEmpleado = fields.Char(string='Nombre', requiered=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', requiered=True, default = fields.date.today())
    direccionEmpleado = fields.Char(string='Dirección', requiered=True)
    telefonoEmpleado = fields.Char(string='Telefono', requiered=True)
    edad = fields.Integer('Edad', compute='_getEdad')

    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for empleado in self:
            empleado.edad = relativedelta(hoy, empleado.fechaNacimiento).years
    
    @api.constrains('dniEmpleado')
    def _checkDNI(self):
        for empleado in self:
            if (len(empleado.dniEmpleado) > 9 ):
                raise exceptions.ValidationError("El DNI no puede ser superior 9 caracteres")
            if (len(empleado.dniEmpleado) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos de 9 caracteres")

    @api.constrains('edad')
    def _checkEdad(self):
        for empleado in self:
            if(empleado.edad < 18):
                raise exceptions.ValidationError("La edad no puede ser inferior a 18")
            
    @api.constrains('telefonoEmpleado')
    def _checkTelefono(self):
        for empleado in self:
            if(len(empleado.telefonoEmpleado) < 9):
                raise exceptions.ValidationError("El telefono no puede tener menos de 9 numeros")
    

    #relaciones entre tablas
    departamento_id = fields.Many2one('proyectos.departamento', string='Empleados')
    proyecto_ids = fields.Many2many('proyectos.proyecto', string='Proyectos')

class proyecto(models.Model):
    _name = 'proyectos.proyecto'
    _description = 'Atributos de un proyecto'
    
    nombreProyecto = fields.Char(string='Nombre proyecto', requiered=True)
    tipoProyecto = fields.Selection(string='Tipo de proyecto', selection=[('f','Front-End'),('b','Back-End')], requiered=True, help='Indica el tipo de proyecto')
    ciudadProyecto = fields.Char(string='Ciudad')
    decripcionProyecto = fields.Text(string='Descripcion del proyecto', help='Indica una descripción del proyecto')
    fechaInicio = fields.Date(string='Fecha Inicio', required=True)
    fechaFin = fields.Date(string='Fecha Final', required=True)

    @api.constrains('fechaInicio')
    def _checkFechaInicio(self):
        hoy = date.today()
        for proyecto in self:
            proyecto.fechaInicio
            dias = relativedelta(hoy, proyecto.fechaInicio).days
            if (dias > 0):
                raise exceptions.ValidationError("La fecha no puede ser anterior a hoy")
            
    @api.constrains('fechaFin')
    def _checkFechaFin(self):
        for proyecto in self:
            if(proyecto.fechaFin < proyecto.fechaInicio):
                raise exceptions.ValidationError("La fecha de finalizacion no puede ser inferior a la de inicio")



    #Relación entre tablas
    empleado_ids = fields.Many2many('proyectos.empleado', string='Empleados')
