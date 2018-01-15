from django.db import models
from django.contrib.auth.models import User
from oferta.models import Ciclo, Curso
from participante.models import Participante
from gestiones.models import Gestion

class Evento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre Evento')
    fecha = models.DateField(verbose_name='Fecha de Curso')
    distrito = models.CharField(max_length=100, verbose_name='Distrito Educativo')
    gestion = models.ForeignKey(Gestion, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    def __unicode__(self):
        return '%s: %s'%(self.user.first_name, self.nombre)
    def __str__(self):
        return '%s: %s' % (self.user.first_name, self.nombre)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['fecha', 'nombre']

class Detalle(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    def __unicode__(self):
        return self.curso
    def __str__(self):
        return self.curso
    class Meta:
        verbose_name_plural = 'Detalle Cursos'
        verbose_name = 'Detalle Curso'
        ordering = ['curso']

class PartEvento(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    cedula = models.CharField(max_length=5000, verbose_name='Cedula de Identidad')
    boleta = models.CharField(max_length=5000, verbose_name='RDA Boleta de Pago')
    f_inscripcion = models.CharField(max_length=5000, verbose_name='Ficha de Inscripcion')
    detalle = models.ForeignKey(Detalle, on_delete=models.PROTECT, null=True)
    def __unicode__(self):
        return self.participante
    def __str__(self):
        return self.participante
    class Meta:
        verbose_name = 'Participante Evento'
        verbose_name_plural = 'Participantes Eventos'
        ordering = ['participante__apellidos', 'participante__nombres']