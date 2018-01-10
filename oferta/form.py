from django import forms
from django.forms import ModelForm

from oferta.models import Ciclo, Curso

class CicloForm(ModelForm):
    class Meta:
        model = Ciclo
        exclude = ['gestion']

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class SearchCiclo(forms.Form):
    ciclo = forms.CharField(max_length=500, label='Ciclo Formativo')