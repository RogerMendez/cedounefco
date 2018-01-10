from django import template
from django.db.models import Q
register = template.Library()

from oferta.models import Curso, Gestion

#@register.filter(name='activo_asignado')
@register.simple_tag
def cant_cours(ciclo):
    cursos = Curso.objects.filter(ciclo=ciclo)
    return cursos.__len__()