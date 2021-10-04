from django.forms import ModelForm

from Atencion.models import Atencion

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = '__all__'