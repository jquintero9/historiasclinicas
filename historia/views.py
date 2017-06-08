# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import PacienteForm, ConsultaForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request,"home.html",{})

@login_required(login_url=reverse_lazy('login'))
def newPaciente(request):

    title = 'Welcome'
    form = PacienteForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }


    #formulario
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request,"formularios.html",context)

@login_required(login_url=reverse_lazy('login'))
def newConsulta(request):

    title = 'Welcome'
    form = ConsultaForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }


    #formulario
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request,"formularios.html",context)
