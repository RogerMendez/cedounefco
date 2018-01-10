from django import forms
from django.forms import ModelForm

from gestiones.models import Gestion

class GestionForm(ModelForm):
    class Meta:
        model = Gestion
        fields = '__all__'