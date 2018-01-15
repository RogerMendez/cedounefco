from django import template
from django.db.models import Q
register = template.Library()

from oferta.models import Curso, Gestion
from evento.models import Detalle

#@register.filter(name='activo_asignado')
@register.simple_tag
def cant_cours(evento):
    cursos = Detalle.objects.filter(evento=evento)
    return cursos.__len__()