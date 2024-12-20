# Generated by Django 5.1.2 on 2024-11-04 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pag', '0002_vacuna_alter_lugaradopcion_options_mascotavacuna'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_preguntas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], max_length=10, null=True)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pag.mascota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=500)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.pregunta')),
                ('solicitud_adopcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitudadopcion')),
            ],
        ),
    ]
