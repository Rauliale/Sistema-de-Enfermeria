from django.urls import path
from Reportes.views import *

app_name = 'reportes'

urlpatterns= [
    #path('',Home, name = 'index.html'),

    path('atencion/reporte/', ReporteAtencionView.as_view(), name='atencion_reporte'),
    #path('atencion/add/', AtencionCreateView.as_view(), name='atencion_create')
]