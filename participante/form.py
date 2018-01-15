from django import forms
from django.forms import ModelForm

from participante.models import Participante

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

class ParticipanteSearch(forms.Form):
    ci = forms.CharField(max_length=10, label='Cedula de Identidad', required = False)
    paterno = forms.CharField(max_length=10, label='Ap. Paterno' , required = False)
    materno = forms.CharField(max_length=10, label='Ap. Materno', required = False)