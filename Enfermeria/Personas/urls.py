from django.urls import path
from Atencion.views import *
from Personas.views import PacienteListView, PacienteCreateView, EnfermeroListView, EnfermeroCreateView

app_name = 'personas'

urlpatterns= [
    path('paciente/list/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente/add/', PacienteCreateView.as_view(), name='paciente_create'),

    path('enfermero/list/', EnfermeroListView.as_view(), name='enfermero_list'),
    path('enfermero/add/', EnfermeroCreateView.as_view(), name='enfermero_create')
]
