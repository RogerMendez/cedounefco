# Generated by Django 2.0.1 on 2018-01-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestion',
            name='gestion',
            field=models.IntegerField(unique=True, verbose_name='Registrar Gestion'),
        ),
    ]
