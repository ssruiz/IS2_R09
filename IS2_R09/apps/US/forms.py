from django.forms.models import ModelForm
from IS2_R09.apps.US.models import us
from django import forms


class us_form(ModelForm):
    class Meta:
        model = us
        
class buscar_us_form(forms.Form):
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())