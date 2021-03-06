# Generated by Django 3.2.7 on 2021-10-05 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id_domicilio', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('nro', models.CharField(max_length=50, verbose_name='Numero')),
                ('mz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Manzana')),
                ('departamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento')),
                ('piso', models.CharField(blank=True, max_length=50, null=True, verbose_name='Piso')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la especialidad')),
                ('descripcion', models.TextField(verbose_name='Descripcion de la especialidad')),
                ('estadoEsp', models.BooleanField(default=True, verbose_name='activo/inactivo')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Guardia',
            fields=[
                ('codGuardia', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo de Guardia')),
                ('fecha', models.DateField(verbose_name='Fecha de Guardia')),
                ('horaInicio', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('provincia', models.CharField(max_length=50, verbose_name='Provincia')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del rol')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion del rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Telefono',
            fields=[
                ('id_tipo_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, choices=[('Fijo', 'Fijo'), ('Movil', 'Movil')], max_length=50, null=True, verbose_name='Tipo')),
                ('empresa', models.CharField(blank=True, choices=[('Tuenti', 'Tuenti'), ('Movistar', 'Movistar'), ('Otro', 'Otro'), ('Personal', 'Personal'), ('Claro', 'Claro')], max_length=50, null=True, verbose_name='Empresa')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('turno', models.CharField(max_length=50, verbose_name='Turno')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('prefijo', models.IntegerField(blank=True, null=True, verbose_name='Prefijo')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('whatsapp', models.BooleanField(default=True, verbose_name='Whatsapp')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('tipo_telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.tipo_telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.domicilio')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.telefono')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'permissions': (('es_Paciente', 'es Paciente'), ('es_pre_Paciente', 'es pre Paciente')),
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.domicilio')),
                ('especialidades', models.ManyToManyField(blank=True, to='Personas.Especialidad')),
                ('guardias', models.ManyToManyField(blank=True, to='Personas.Guardia')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.telefono')),
                ('turno', models.ManyToManyField(blank=True, to='Personas.Turno')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medico',
                'permissions': (('es_Medico', 'es Medico'), ('es_pre_Medico', 'es pre Medico')),
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.domicilio')),
                ('guardias', models.ManyToManyField(blank=True, to='Personas.Guardia')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.telefono')),
                ('turno', models.ManyToManyField(blank=True, to='Personas.Turno')),
            ],
            options={
                'verbose_name': 'Enfermero',
                'verbose_name_plural': 'Enfermeros',
                'permissions': (('es_Enfermero', 'es Enfermero'), ('es_pre_Enfermero', 'es pre Enfermero')),
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('codAsistencia', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsistencia', models.DateField(verbose_name='Fecha de Asistencia')),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('codGuardia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.guardia')),
            ],
        ),
    ]
