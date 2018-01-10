from django.db import models

class Gestion(models.Model):
    gestion = models.IntegerField(verbose_name='Registrar Gestion', unique=True)
    def __str__(self):
        return '%s'%self.gestion
    class Meta:
        verbose_name = 'Gestion'
        verbose_name_plural = 'Gestiones'
        ordering = ['gestion']