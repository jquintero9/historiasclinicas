# -*- coding: utf-8 -*-
# usuarios/views
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .forms import (
    MedicoForm,
    LoginForm,
    BusquedaPacienteForm,
    FormBusquedaPaciente,
)
from .models import Medico
#from .utils import enviar_email, get_namespace, get_objects
#Importamos la vista genérica FormView
from django.views.generic.edit import FormView
#Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm


def cuentaInactiva(request):
    return render(request,"cuenta_inactiva.html",{})

def newMedico(request):

    title = 'Welcome'
    form = MedicoForm(data=request.POST)
    model = Medico
    context = {
        "title": title,
        "form": form,
    }

    #formulario
    if form.is_valid():

        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()

        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        context = {
            "title": title,
            "form": form,
        }

        return render(request,"formularios.html",context)


class InicioSesion(View):

    """
    Auntentica los usuairos de tipo Administrador y Vendedor.
    """

    template_name = 'login.html'
    form_class = None
    success_url = None

    def get(self, request):

        """
        Procesa la petición HTTP por el método GET.
        Se instancia el formulario de inicio de sesión y se envía
        al template.
        Si ya hay una sesión iniciada entonces se redirige al usuario a su vista correspondiente.
        :param request: Contiene la información de la petición HTTP.
        :return: La vista Registrar Vendedor.
        """

        if not request.user.is_authenticated():

            self.form_class = LoginForm()
            context = {'form': self.form_class}

            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect(reverse_lazy('home'))

    def post(self, request):

        """
        Procesa los datos que llengan por el formulario mediante el
        método POST.
        Se instancia el formulario de Inicio de Sesión, para validar los datos.
        Luego se verifica el estado de la cuenta del usuario, su está activa
        Se crea la sesión y se redirecciona a su respectiva vista y de lo contrario
        no se permite el acceso a la aplicación.

        :param request: Contiene la información de la petición HTTP.
        :return: Se redirecciona a la vista del usuairo o se retorna el formulario.
        """

        self.form_class = LoginForm(data=request.POST)

        if self.form_class.is_valid():
            username = self.form_class.cleaned_data.get('username')
            password = self.form_class.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user=user)
                    return HttpResponseRedirect(reverse_lazy('home'))
                else:
                    return HttpResponseRedirect(reverse_lazy('inactiva'))
            else:
                messages.error(request, u'El nombre de usuario y/o la contraseña no coinciden.')

        context = {'form': self.form_class}

        return render(request,"home.html",context)

@login_required(login_url=reverse_lazy('login'))
def cerrar_sesion(request):
    """
    Verifca el permiso del usuario que está intentado acceder a la vista.
    Si el permiso no es válido deniega el acceso.
    Cierra la sesión actual y redirecciona al usuario a la vista de inicio de sesión.
    """
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login'))
    else:
        raise PermissionDenied