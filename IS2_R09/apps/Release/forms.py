"""
Created on 15/5/2015
Modulo que define los formularios usados en las L{views<IS2_R09.apps.Release.views>} de los B{Release}.  
    @author: Samuel Ruiz,Melissa Bogado, Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.forms.models import ModelForm
from IS2_R09.apps.Release.models import release
from django import forms

class release_form(ModelForm):
    version = forms.CharField (widget=forms.TextInput (attrs={'class':'campos'}))
    fecha_creacion = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos'}))
    sprints_asociados = forms.CharField(widget=forms.TextInput(attrs={'class': 'campos'}))
    us_asociados = forms.CharField(widget=forms.TextInput(attrs={'class': 'campos'}))
    class Meta:
        model = release
        labels = {
            'version':('Version'),
            'fecha_creacion':('Fecha de Creacion'),
            'sprints_asocaidos':('Sprints Asociados'),
            'us_asociados': ('US Asociados'),
        }

#------------------------------------------------------------------------------------
class consultar_release_form(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    version = forms.CharField(label='Version',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_creacion = forms.CharField(label='Fecha de Creacion',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    sprints_asociados = forms.CharField(label='Sprints Asociados',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    us_asociados = forms.CharField(label='US Asociados',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = release
        fields = ('id','version','fecha_creacion','sprints_asociados','us_asociados')        

#------------------------------------------------------------------------------------

class modificar_release_form (forms.Form):
    version = forms.CharField(label = 'Version',widget=forms.TextInput(attrs={'class':'campos'}))
    fecha_creacion =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    sprints_asociado =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    us_asociado =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    
    class Meta:
        model = release
        widgets = {
                   'version' : forms.TextInput(attrs={'class': 'campos'}),
                   'fecha_creacion': forms.TextInput(attrs={'class': 'campos'}),
                   'sprints_asociados' : forms.TextInput(attrs={'class': 'campos'}),
                   'us_asociados' : forms.TextInput(attrs={'class': 'campos'}),
                   'descripcion' : forms.Textarea(attrs={'class': 'textarea'}),
                   }

#class eliminar_release_form (forms.Form):
#---------------------------------------------------------------------------------------------------------------------
class buscar_release_form(forms.Form):
    BUSCAR_POR = {
                  ('id_release','ID Release'),
                  ('version','Version'),
                  ('sprints_asociado','Sprints Asociados'),
                  ('us_asociado','US Asociados'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    
    busqueda = forms.CharField(widget=forms.TextInput())