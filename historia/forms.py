from django import forms

from .models import Paciente
from .models import Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            "identificacion",
            "apellidos",
            "nombres",
            "estado_civil",
            "fecha_nacimiento",
            "edad",
            "sexo",
            "ocupacion",
            "direccion",
            "telefono",
            "aseguradora",
            "nombre_acomp",
            "tel_acomp",
        ]

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            "paciente",
            "tipo_consulta",
            "codigo_especialidad",
            "dias_incapacidad",
            "condicion_usuaria",
            "conducta",
            "causa_extrema",
            "codigo_diagnostico",
            "tipo_diagnostico",
            "consulta_anual",
        ]
