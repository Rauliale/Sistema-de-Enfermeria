from crum import get_current_user
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
import calendar
from django.forms.models import model_to_dict


from user.models import BaseModel



class Turno(models.Model):
    id_turno=models.AutoField(primary_key=True)
    turno=models.CharField('Turno', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.turno

class Guardia(models.Model):
    codGuardia = models.AutoField('Codigo de Guardia', primary_key = True, null = False, blank = False)
    fecha = models.DateField('Fecha de Guardia', null = False, blank = False)
    horaInicio = models.TimeField()

    def __str__(self):
        return str(self.fecha) + ' - ' + str(self.horaInicio) 

class Asistencia(models.Model):
    codAsistencia=models.AutoField(primary_key=True)
    codGuardia=models.ForeignKey(Guardia, on_delete=models.PROTECT,null=True)
    fechaAsistencia = models.DateField('Fecha de Asistencia', null = False, blank = False)
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()

    
    def __str__(self):
        return self.fechaAsistencia
    

class Provincia(models.Model):
    id_provincia=models.AutoField(primary_key=True)
    provincia=models.CharField('Provincia', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.provincia

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key = True)
    localidad=models.CharField('Localidad', max_length=50,blank=False,null=False)
    provincia=models.ForeignKey(Provincia,on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    def __str__(self):
        return self.localidad

class Domicilio(models.Model):
    id_domicilio = models.AutoField(primary_key=True)
    calle=models.CharField('Calle', max_length=100,blank=False,null=False)
    nro=models.CharField('Numero', max_length=50,blank=False,null=False)
    mz = models.CharField('Manzana', max_length=50,null=True,blank=True)
    departamento=models.CharField('Departamento', max_length=50,null=True,blank=True)
    piso=models.CharField('Piso', max_length=50,null=True,blank=True)
    borrado = models.BooleanField('borrado',default=False)
    
    def __str__(self):
        return 'calle '+ self.calle + ' - ' + str(self.nro)

class Tipo_Telefono(models.Model):
    TIPO={
        ('Movil','Movil'),
        ('Fijo','Fijo')
    }
    EMPRESA={
        ('Personal','Personal'),
        ('Claro','Claro'),
        ('Movistar','Movistar'),
        ('Tuenti','Tuenti'),
        ('Otro','Otro')
    }
    id_tipo_telefono=models.AutoField(primary_key=True)
    tipo=models.CharField('Tipo', max_length=50,blank=True,null=True,choices=TIPO)
    empresa=models.CharField('Empresa', max_length=50,blank=True,null=True,choices=EMPRESA)
    borrado = models.BooleanField('borrado',default=False)

    
    def __str__(self):
        return self.tipo

class Telefono(models.Model):
    id_telefono=models.AutoField(primary_key=True)
    prefijo=models.IntegerField('Prefijo',blank=True,null=True)
    numero=models.IntegerField('Numero',null=True,blank=True)
    whatsapp=models.BooleanField('Whatsapp',default=True)
    tipo_telefono=models.ForeignKey(Tipo_Telefono, on_delete=models.PROTECT,null=True)
    borrado = models.BooleanField('borrado',default=False)    
    # miembro no def :C contacto= models.ForeignKey(Miembro, on_delete=models.PROTECT,null=True) #tel de contacto en caso de necesitar
    
    def __str__(self):
        return str(self.prefijo) + ' - ' + str(self.numero) 



class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del rol', max_length = 100, null = False, blank = False)
    descripcion = models.TextField('Descripcion del rol', null = True, blank = True)
    

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.descripcion = (self.descripcion).upper()
        return super(Rol, self).save(*args, **kwargs)


class Paciente(BaseModel):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        permissions = (("es_Paciente", "es Paciente"),("es_pre_Paciente", "es pre Paciente"))

    def __str__(self):
            return str(self.nombre) + ' ' + str(self.apellido )
            #return self.apellido

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def save(self, force_incert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:    
            if not self.pk:
                self.user.cretion = user
            else:
                self.user_update = user
        super(Paciente, self).save()



class Especialidad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la especialidad', max_length = 100, null = False, blank = False)
    descripcion = models.TextField('Descripcion de la especialidad', null = False, blank = False)
    estadoEsp = models.BooleanField('activo/inactivo', default = True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        


    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.descripcion = (self.descripcion).upper()
        return super(Especialidad, self).save(*args, **kwargs)

class Enfermero(models.Model):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    turno = models.ManyToManyField(Turno, blank = True)
    guardias = models.ManyToManyField(Guardia, blank = True)
    #especialidades = models.ManyToManyField(Especialidad, blank = True)

    class Meta:
        verbose_name = 'Enfermero'
        verbose_name_plural = 'Enfermeros'
        permissions = (("es_Enfermero", "es Enfermero"),("es_pre_Enfermero", "es pre Enfermero"))

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre
        #return self.apellido

class Medico(models.Model):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    turno = models.ManyToManyField(Turno, blank = True)
    especialidades = models.ManyToManyField(Especialidad, blank = True)
    guardias = models.ManyToManyField(Guardia, blank = True)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medico'
        permissions = (("es_Medico", "es Medico"),("es_pre_Medico", "es pre Medico"))

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre
        #return self.apellido
