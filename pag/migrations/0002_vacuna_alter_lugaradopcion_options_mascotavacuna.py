# Generated by Django 5.1.2 on 2024-10-17 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vacuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='lugaradopcion',
            options={'verbose_name_plural': 'Lugares de Adopcion'},
        ),
        migrations.CreateModel(
            name='MascotaVacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aplicacion', models.DateTimeField()),
                ('fecha_proxima', models.DateTimeField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pag.mascota')),
                ('vacuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pag.vacuna')),
            ],
        ),
    ]
