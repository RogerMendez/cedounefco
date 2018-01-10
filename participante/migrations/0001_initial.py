# Generated by Django 2.0.1 on 2018-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=15, verbose_name='Cedula de Identidad')),
                ('rda', models.IntegerField(blank=True, null=True, verbose_name='RDA')),
                ('nombre1', models.CharField(max_length=100, verbose_name='Primer Nombre')),
                ('nombre2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('paterno', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ap. Paterno')),
                ('materno', models.CharField(max_length=100, verbose_name='Ap. Materno')),
                ('tipo', models.CharField(choices=[('Maestra/o', 'Maestra/o'), ('Administrativo', 'Administrativo'), ('Estudiante', 'Estudiante'), ('Otro', 'Otro')], max_length=20, verbose_name='Tipo Participante')),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'Femenino')], max_length=20, null=True, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ['paterno', 'materno', 'nombre1', 'nombre2'],
            },
        ),
    ]