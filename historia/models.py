# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paciente(models.Model):
    """Datos del paciente."""
    identificacion = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    nombres = models.CharField(max_length=120)
    estado_civil = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    edad = models.CharField(max_length=120)
    sexo = models.CharField(max_length=120)
    ocupacion = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=120)
    aseguradora = models.CharField(max_length=120)
    nombre_acomp = models.CharField(max_length=120)
    tel_acomp = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    def __unicode__(self):
        return str(self.identificacion)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null = True)
    """Atencion."""
    tipo_consulta = models.CharField(max_length=120)
    codigo_especialidad = models.CharField(max_length=120)
    dias_incapacidad = models.CharField(max_length=120)
    CONDICION_USUARIA_CHOICES = (
        (1,'Embarazo 1er trimestre'),
        (2,'Embarazo 2do trimestre'),
        (3,'Embarazo 3er trimestre'),
        (4,'No embarazada'),
    )
    condicion_usuaria = models.CharField(max_length=120,
        choices = CONDICION_USUARIA_CHOICES,
        default = 4
    )
    CONDUCTA_CHOICES = (
        (1,'Prescripcion IPS de medicamentos'),
        (2,'Ordenacion de procedimientos diagnosticos'),
        (3,'Ordenacion de procedimientos terapeuticos'),
        (4,'Remision'),
        (5,'Interconsulta'),
        (6,'Contrereferencia'),
        (7,'Orden de hospitalizacion'),
        (8,'Control'),
        (9,'Ninguna'),
    )
    conducta = models.CharField(max_length=120,
        choices = CONDUCTA_CHOICES,
        default = 9,
    )
    """Motivo de la consulta."""
    CAUSA_EXTREMA_CHOICES = (
        (1,'Accidente de IPS trabajo'),
        (2,'Accidente de transito'),
        (3,'Otro tipo de accidente'),
        (4,'Evento catastrofico'),
        (5,'Lesion por agresion'),
        (6,'Lesion auto inflingida'),
        (7,'Maltrato'),
        (8,'Enfermedad general'),
        (9,'Enfermedad profesional'),
        (10,'Otra'),
    )
    causa_extrema = models.CharField(max_length=120,
        choices = CAUSA_EXTREMA_CHOICES,
        default = 10,
    )
    codigo_diagnostico = models.CharField(max_length=120)
    TIPO_DIAGNOSTICO_CHOICES = (
        ('I','Impresion diagnostica'),
        ('N','Confirmado nuevo'),
        ('R','Confirmado repetido'),
    )
    tipo_diagnostico = models.CharField(
        choices = TIPO_DIAGNOSTICO_CHOICES,
        max_length = 1,
        default = 'I',
    )
    CONSULTA_ANUAL_CHOICES = (
        ('P','Primera vez'),
        ('R','Repetida'),
    )
    consulta_anual = models.CharField(
        choices = CONSULTA_ANUAL_CHOICES,
        max_length = 1,
        default = 'P',
    )
    def __unicode__(self):
        return str(self.paciente)
