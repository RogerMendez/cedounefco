from django import forms
from django.forms import ModelForm, TextInput

from evento.models import Evento, Detalle, PartEvento

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        exclude = ['user', 'gestion']
        widgets = {
            'fecha': TextInput(attrs={'type': 'date'}),
        }