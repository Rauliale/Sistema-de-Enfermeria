# Generated by Django 3.2.7 on 2021-10-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0004_auto_20211001_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Claro', 'Claro'), ('Movistar', 'Movistar'), ('Personal', 'Personal'), ('Otro', 'Otro'), ('Tuenti', 'Tuenti')], max_length=50, null=True, verbose_name='Empresa'),
        ),
    ]
