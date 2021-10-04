from django.forms import ModelForm

from Personas.models import Paciente, Enfermero


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class EnfermeroForm(ModelForm):
    class Meta:
        model = Enfermero
        fields = '__all__'