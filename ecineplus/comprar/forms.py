from django import forms
from .models import Boleto

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ['id_Boleto','cliente','pelicula','precio','asiento']

      