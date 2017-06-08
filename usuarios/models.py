# -*- coding: utf-8 -*-
# usuarios/models
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.core.validators import RegexValidator
from datetime import datetime

class Medico(models.Model):

    doc=(
        ('CC','CEDULA DE CIUDADANIA'),
        ('CE','CEDULA DE EXTRANGERIA'),
        ('NI','NIT'),
        ('PA','PASAPORTE'),
    )
    genero=(
        ('H','HOMBRE'),
        ('M','MUJER'),
        ('O','OTRO'),
    )
    birthday = models.DateField(default="1980-04-28")
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    REQUIRED_FIELDS = ['user']
    direccion = models.CharField(max_length=40,default='villa x cs 10')
    phone = models.CharField(max_length=10,default='3333333')
    type_doc = models.CharField(max_length=2,choices=doc,default='CC')
    type_gen = models.CharField(max_length=1, choices=genero, default='H')
    def __str__(self):
        return self.user.username

