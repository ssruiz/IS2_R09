'''
Created on 23/4/2015

@author: meliam
'''
from django.forms.models import ModelForm
from IS2_R09.apps.Sprint.models import sprint
from django import forms

"""Muestra los formularios de Sprint.
   
"""

class sprint_form(ModelForm):
    fecha_inicio = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_fin = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    # release_asociado = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'textarea'}))
    #flujo_asociado = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = sprint
        fields = '__all__'
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class':'campos'}),
                   'descripcion' : forms.Textarea(attrs={'class':'textarea'}),
                   }

#------------------------------------------------------------------------------------
class consultar_sprint_form(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_creacion = forms.CharField(label='Fecha de Creacion',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_inicio = forms.CharField(label='Fecha de Inicio',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_fin = forms.CharField(label='Fecha de Finalizacion',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #release_asociado = forms.CharField(label='Release Asociado',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #flujo_asociado = forms.CharField(label='Flujo Asociado',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = sprint
        fields = '__all__'
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class':'campos','readonly':'readonly'}),
                   'descripcion' : forms.Textarea(attrs={'class':'textarea','readonly':'readonly'}),
                   }
#    help_texts = {
#           'username': (''),
#      }
        

#------------------------------------------------------------------------------------
class buscar_sprint_form(forms.Form):
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())