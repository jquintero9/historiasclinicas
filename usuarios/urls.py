# -*- coding: utf-8 -*-
# usuarios/urls

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from views import InicioSesion


urlpatterns = [
	url(r'^newmedico/$', views.newMedico, name="newmedico"),
	url(r'^login/$', InicioSesion.as_view(), name="login"),
	url(r'^logout/$', views.cerrar_sesion, name="logout"),
	url(r'^cuenta_inactiva/$', views.cuentaInactiva, name="inactiva"),
]