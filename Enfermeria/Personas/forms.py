from django.forms import ModelForm

from Personas.models import Paciente, Enfermero
from django.forms.widgets import DateInput, TextInput, Textarea
from datetime import datetime


#class PacienteForm(ModelForm):
#    class Meta:
#        model = Paciente
#        fields = '__all__'

class PacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['dni'].widget.attrs['autofocus'] = True

    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',

                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Apellido',
                    'rows': 3,
                    'cols': 3
                }
            ),
            'fechaNac': DateInput(format='%d/%m/%Y',
                                       attrs={
                                           'value': datetime.now().strftime('%d/%m/%Y'),
                                       }
                                       ),
        }
        exclude = ['user_creation', 'user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



class EnfermeroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['dni'].widget.attrs['autofocus'] = True

    class Meta:
        model = Enfermero
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Apellido',
                    'rows': 3,
                    'cols': 3
                }
            ),
            'fechaNac': DateInput(format='%d/%m/%Y',
                                       attrs={
                                           'value': datetime.now().strftime('%d/%m/%Y'),
                                       }
                                       ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data