from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from Personas.models import Enfermero, Paciente
from Personas.forms import EnfermeroForm, PacienteForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/list.html'
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
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
        context['create_url'] = reverse_lazy('personas:paciente_create')
        context['list_url'] = reverse_lazy('personas:paciente_list')
       
        return context

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'Paciente/create.html'
    success_url = reverse_lazy('paciente_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Paciente'
        context['create_url'] = reverse_lazy('personas:paciente_create')
        context['list_url'] = reverse_lazy('personas:paciente_list')
        context['action'] = 'add'
        return context

########################### Enfermero ##########################
class EnfermeroListView(ListView):
    model = Enfermero
    template_name = 'enfermero/list.html'
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
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
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Enfermero'
        context['create_url'] = reverse_lazy('personas:enfermero_create')
        context['list_url'] = reverse_lazy('personas:enfermero_list')
        context['action'] = 'add'
        return context


    
