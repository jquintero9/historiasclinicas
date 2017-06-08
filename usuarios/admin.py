# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
	Medico,
)

class MedicoAdmin(admin.ModelAdmin):

    list_display = ['user']

    class Meta:
        model = Medico

admin.site.register(Medico, MedicoAdmin)
