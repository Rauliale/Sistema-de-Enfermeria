from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

from Personas.models import Paciente, Enfermero, Medico
from django.forms.models import model_to_dict

from user.models import BaseModel



# Create your models here.


class Enfermedad(models.Model):
    codEnfermedad = models.AutoField('Codigo de Enfermedad', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre Enfermedad', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedad'
    
    def __str__(self):
        return str(self.codEnfermedad) + ' - ' + str(self.nombre)



class UnidadMedida(models.Model):
    codUnidadMedida = models.AutoField('Codigo de Medida', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre Unidad Medida', max_length = 100, null = False, blank = False)



class Medicacion(models.Model):
    codMedicacion = models.AutoField('Codigo de Medicacion', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre Medicacion', max_length = 100, null = False, blank = False)
    dosis = models.CharField('Dosis Medicacion', max_length = 100, null = False, blank = False)
    repetirDosis = models.CharField('Repetir dosis Medicacion', max_length = 100, null = False, blank = False)
    cadaCuanto = models.CharField('Horas Nueva dosis', max_length = 100, null = False, blank = False)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete = models.PROTECT)

    class Meta:
        verbose_name = 'Medicacion'
        verbose_name_plural = 'Medicacion'
    
    def __str__(self):
        return str(self.codMedicacion) + ' - ' + str(self.nombre)

class Sintoma(models.Model):
    codSintoma = models.AutoField('Codigo de Sintoma', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre Sintoma', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Nombre Sintoma', max_length = 200, null = False, blank = False)

    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = 'Sintoma'
    
    def __str__(self):
        return str(self.codSintoma) + ' - ' + str(self.nombre)


class Alergia(models.Model):
    codAlergia = models.AutoField('Codigo Alergia', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre Alergia', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Alergia'
        verbose_name_plural = 'Alergia'
    
    def __str__(self):
        return str(self.codAlergia) + ' - ' + str(self.nombre)



class HistoriaClinica(models.Model):
    codHistoriaClinica = models.AutoField('Codigo de H.C.', primary_key = True, null = False, blank = False)
    fechaInicio = models.DateField('Fecha de Inicio', null = False, blank = False)
    enfermedades = models.ManyToManyField(Enfermedad, blank = True)
    medicacion = models.ManyToManyField(Medicacion, blank = True)
    alergia = models.ManyToManyField(Alergia, blank = True)

    paciente = models.ForeignKey(Paciente, on_delete = models.PROTECT)
    #history = HistoricalRecords()

    class Meta:
        verbose_name = 'HistoriaClinica'
        verbose_name_plural = 'HistoriaClinica'
    
    def __str__(self):
        return str(self.codHistoriaClinica) + ' - ' + str(self.paciente)

class Atencion(models.Model):
    codAtencion = models.AutoField('Codigo de Atencion', primary_key = True, null = False, blank = False)
    date_joined = models.DateField('Fecha de Ingreso', default=datetime.now, null = False, blank = False)
    motivoAtencion = models.CharField('Motivo de la atencion', max_length = 120, null = False, blank = False)
    temperatura = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    tensionArterial = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    frecuenciaCardiaca = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    saturacionOxigeno = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    historiaClinica = models.ForeignKey(HistoriaClinica, on_delete = models.PROTECT)
    enfermero = models.ForeignKey(Enfermero, on_delete = models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete = models.PROTECT)
    medicacion = models.ManyToManyField(Medicacion, blank = True)
    sintomas = models.ManyToManyField(Sintoma, blank = True)
    

    def __str__(self):
        return str(self.codAtencion) + ' - ' + str(self.date_joined)

    def toJSON(self):
        item = model_to_dict(self)
        #item['historiaClinica'] = self.historiaClinica.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item