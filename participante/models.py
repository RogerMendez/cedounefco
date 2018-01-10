from django.db import models

TYPES_PART = (
    ('Maestra/o','Maestra/o'),
    ('Administrativo', 'Administrativo'),
    ('Estudiante','Estudiante'),
    ('Otro', 'Otro'),
)
TYPES_SEX = (
    ('1', 'Masculino'),
    ('2', 'Femenino'),
)

class Participante(models.Model):
    ci = models.CharField(max_length=15, verbose_name='Cedula de Identidad')
    rda = models.CharField(max_length=20, verbose_name='RDA', null=True, blank=True)
    nombre1 = models.CharField(max_length=100, verbose_name='Primer Nombre')
    nombre2 = models.CharField(max_length=100, verbose_name='Segundo Nombre', blank=True, null=True)
    paterno = models.CharField(max_length=100, verbose_name='Ap. Paterno', blank=True, null=True)
    materno = models.CharField(max_length=100, verbose_name='Ap. Materno')
    tipo = models.CharField(max_length=20, verbose_name='Tipo Participante', choices=TYPES_PART)
    sexo = models.CharField(max_length=20, verbose_name='Sexo', choices=TYPES_SEX, null=True, blank=True)
    def __str__(self):
        return '%s %s %s %s'%(self.paterno, self.materno, self.nombre1, self.nombre2)
    def __unicode__(self):
        return '%s %s %s %s' % (self.paterno, self.materno, self.nombre1, self.nombre2)
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['paterno', 'materno', 'nombre1', 'nombre2']