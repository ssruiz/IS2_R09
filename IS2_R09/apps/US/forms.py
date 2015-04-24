# -*- encoding: utf-8 -*-

"""
    Modulo que define los formularios usados en las L{views<IS2_R09.apps.US.views>} de los B{User Stories}.  
    @author: Samuel Ruiz,Melissa Bogado, Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.forms.models import ModelForm
from IS2_R09.apps.US.models import us
from django import forms


class us_form(ModelForm):
    """
        Formulario creado a partir del modelo de un User Story y utilizado en 
        creación de User Story
    """
    class Meta:
        model = us

class mod_us_form(ModelForm):
    """
        Formulario creado a partir del modelo de un User Story y utilizado en la 
        modificación de User Story
    """
    class Meta:
        model = us
        widgets = {
                   'proyecto_asociado' : forms.Select(attrs={'readonly':'readonly','disable':'disable'}),
                   }
        localized_fields = ('proyecto_asociado',)
        
class buscar_us_form(forms.Form):
    """
        Formulario creado para búsqueda de User Story por nombre
    """
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())
    
class consultar_form(ModelForm):
    class Meta:
        model = us
        widgets = {
                   'nombre' : forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'descripcion' : forms.Textarea(attrs={'readonly':'readonly','class': 'textarea'}), 
                   'tiempo_estimado' : forms.NumberInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'tiempo_trabajado' : forms.NumberInput(attrs={'readonly':'readonly','class': 'campos'}), 
                   'usuario_asiganado': forms.SelectMultiple(attrs={'readonly':'readonly'}),
                   'prioridad': forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'flujo_asignado': forms.SelectMultiple(attrs={'readonly':'readonly'}),
                   'proyecto_asignado': forms.SelectMultiple(attrs={'readonly': 'readonly'}),
                   }
        
class modificar_form(ModelForm):
    
    class Meta:
        model = us
        exclude = ['usuario_asignado',]
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class': 'campos'}),
                   'descripcion' : forms.Textarea(attrs={'class': 'textarea'}),
                   'tiempo_estimado' : forms.NumberInput(attrs={'class': 'campos'}),
                   'tiempo_trabajado' : forms.NumberInput(attrs={'class': 'campos'}),
                   'prioridad' : forms.TextInput(attrs={'class': 'campos'}),
                   }

