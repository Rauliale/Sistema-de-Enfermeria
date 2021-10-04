from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from Personas.models import Enfermero, Paciente
from Personas.forms import EnfermeroForm, PacienteForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Paciente.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_queryset(self):
        return Paciente.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pacientes'
       
        return context

class PacienteCreateView(CreateView):
   model = Paciente
   form_class = PacienteForm
   template_name = 'Paciente/create.html'
   success_url = reverse_lazy('paciente_list')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Creación un Paciente'
       return context

########################### Enfermero ##########################
class EnfermeroListView(ListView):
    model = Enfermero
    template_name = 'enfermero/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Enfermero.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_queryset(self):
        return Enfermero.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Enfermero'
       
        return context

class EnfermeroCreateView(CreateView):
   model = Enfermero
   form_class = EnfermeroForm
   template_name = 'Enfermero/create.html'
   success_url = reverse_lazy('enfermero_list')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Creación un Enfermero'
       return context
   

    
