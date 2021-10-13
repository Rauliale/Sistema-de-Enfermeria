from django.forms import ModelForm

from Atencion.models import *


from django.forms.widgets import DateInput, Select, SelectMultiple, TextInput, Textarea
from datetime import datetime


#class AtencionForm(ModelForm):
#    class Meta:
#        model = Atencion
#        fields = '__all__'

class AtencionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['motivoAtencion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Atencion
        fields = '__all__'
        widgets = {
            'historiaClinica': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'enfermero': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'medico': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'medicacion': SelectMultiple(
                attrs={
                    'class': "js-example-basic-multiple", 
                    'multiple':'multiple',
                    'placeholder' : 'Seleccione medicacion'
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