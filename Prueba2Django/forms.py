from django import forms
from Prueba2Django.models import Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model=Seminario
        fields='__all__'
        
        