from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from Atencion.models import Atencion
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from Atencion.forms import AtencionForm

# Create your views here.
#Home
def Home(request):
    return render(request, 'index.html')


########################### Atencion ##########################
class AtencionListView(ListView):
    model = Atencion
    template_name = 'Atencion/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Atencion.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_queryset(self):
        return Atencion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Atencion'
       
        return context


class AtencionCreateView(CreateView):
   model = Atencion
   form_class = AtencionForm
   template_name = 'Atencion/create.html'
   success_url = reverse_lazy('atencion_list')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Creación un Atencion'
       return context
