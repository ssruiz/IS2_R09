# -*- encoding: utf-8 -*-
from django.forms.models import ModelForm
from IS2_R09.apps.Flujo.models import flujo,actividad
from django import forms


class flujo_form(ModelForm):
    '''
        Formulario que usado en la creacion de flujos
    '''
    class Meta:
        model = flujo
        widgets = {
                   'actividades': forms.CheckboxSelectMultiple()
                   }
class actividad_form(ModelForm):
    class Meta:
        model = actividad
        
class buscar_flujo_form(forms.Form):
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())

class consultar_form(ModelForm):
    '''
        Formulario que usado en la creacion de flujos
    '''
    class Meta:
        model = flujo
        widgets = {
                   'actividades': forms.CheckboxSelectMultiple(attrs={'readonly':'readonly'}),
                   'nombre' : forms.TextInput(attrs={'readonly':'readonly'}),
                   }
