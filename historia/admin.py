# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Paciente
from .models import Consulta

admin.site.register(Paciente)
admin.site.register(Consulta)
