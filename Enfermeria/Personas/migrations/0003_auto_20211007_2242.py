# Generated by Django 3.2.7 on 2021-10-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0002_auto_20211007_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Tuenti', 'Tuenti'), ('Claro', 'Claro'), ('Otro', 'Otro'), ('Personal', 'Personal'), ('Movistar', 'Movistar')], max_length=50, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='tipo_telefono',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Movil', 'Movil'), ('Fijo', 'Fijo')], max_length=50, null=True, verbose_name='Tipo'),
        ),
    ]