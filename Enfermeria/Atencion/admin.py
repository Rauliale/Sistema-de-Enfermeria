from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Sintoma)
admin.site.register(Enfermedad)
admin.site.register(Medicacion)
admin.site.register(Alergia)

admin.site.register(HistoriaClinica)
admin.site.register(Atencion)