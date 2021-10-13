from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from Atencion.models import Atencion
from Reportes.forms import ReporteForm
from django.db.models.functions import Coalesce
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required
#from django.db.models.functions import Coalesce
#from django.db.models import Sum


class ReporteAtencionView(TemplateView):
    template_name = 'Reportes/reporte.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Atencion.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.codAtencion,
                        s.historiaClinica.paciente.nombre,
                        s.historiaClinica.paciente.apellido,
                        s.date_joined.strftime('%Y-%m-%d'),
                        s.motivoAtencion,
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Atenciones'
        context['entity'] = 'Reportes'
        #context['list_url'] = reverse_lazy('atencion_reporte')
        context['form'] = ReporteForm()
        return context
