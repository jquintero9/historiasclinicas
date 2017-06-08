# -*- coding: utf-8 -*-
# usuarios/forms
from __future__ import unicode_literals

from django import forms
from .models import Medico
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, RegexValidator

class MedicoForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'validator'
            }
        ),
    )

    password = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput()
    )


class BusquedaPacienteForm(forms.Form):

    busqueda = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'type': 'search', 'placeholder': u'Buscar por cédula'}),
    )


class FormBusquedaPaciente(forms.Form):
    cedula = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': u'Ingrese el número de cédula'}),
    )