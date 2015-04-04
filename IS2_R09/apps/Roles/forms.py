from django.forms.models import ModelForm
from django.contrib.auth.models import Group

from django import forms
import datetime
class group_form(ModelForm):
    now = datetime.datetime.now().date()
    class Meta:
        model = Group
        fields = ('name','permissions',)
        widgets = {
                   'permissions' : forms.CheckboxSelectMultiple(),
                   }

class consultar_rol_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Group
        fields = ('name','permissions',)
        widgets = {
                   'permissions' : forms.CheckboxSelectMultiple(attrs={'readonly':'readonly'}),
                   }

class buscar_rol_form(forms.Form):
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())