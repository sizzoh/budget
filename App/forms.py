from django.forms import ModelForm
from .models import employee

class customForm(ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        