from django.db import models

from gestiones.models import Gestion

class Ciclo(models.Model):
    ciclo = models.CharField(max_length=500, verbose_name='Ciclo Formativo')
    gestion = models.ForeignKey(Gestion, verbose_name='Gestion', on_delete=models.CASCADE)
    def __unicode__(self):
        return self.ciclo
    def __str__(self):
        return self.ciclo
    class Meta:
        verbose_name = 'Ciclo'
        verbose_name_plural = 'Ciclos'
        ordering = ['ciclo']

class Curso(models.Model):
    curso = models.CharField(max_length=500, verbose_name='Curso Formativo')
    ciclo = models.ForeignKey(Ciclo, verbose_name='Seleccion Ciclo', on_delete=models.PROTECT)
    def __unicode__(self):
        return self.curso
    def __str__(self):
        return self.curso
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['curso']