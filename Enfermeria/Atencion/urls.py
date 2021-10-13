from django.urls import path
from Atencion.views import *

app_name = 'atencion'

urlpatterns= [
    path('',Home, name = 'index'),

    path('atencion/list/', AtencionListView.as_view(), name='atencion_list'),
    path('atencion/add/', AtencionCreateView.as_view(), name='atencion_create')
]
