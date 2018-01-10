from django import forms
from django.forms import ModelForm

from participante.models import Participante

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'
