# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(default='1980-04-28')),
                ('direccion', models.CharField(default='villa x cs 10', max_length=40)),
                ('phone', models.CharField(default='3333333', max_length=10)),
                ('type_doc', models.CharField(choices=[('CC', 'CEDULA DE CIUDADANIA'), ('CE', 'CEDULA DE EXTRANGERIA'), ('NI', 'NIT'), ('PA', 'PASAPORTE')], default='CC', max_length=2)),
                ('type_gen', models.CharField(choices=[('H', 'HOMBRE'), ('M', 'MUJER'), ('O', 'OTRO')], default='H', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]