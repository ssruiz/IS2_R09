from django.forms.models import ModelForm
from IS2_R09.apps.Sprint.models import sprint
from django import forms

"""Muestra los formularios de Sprint.
   
"""

class sprint_form(ModelForm):
#    nombre = forms.CharField (widget=forms.Textarea (attrs={'class':'textarea'}))
    fecha_creacion = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_inicio = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_fin = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos'}))
    # release_asociado = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'textarea'}))
    flujo_asociado = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = sprint
        labels = {
            'fecha_creacion':('Fecha de Creacion'),
            'fecha_inicio':('Fecha de Inicio'),
            'fecha_fin':('Fecha de Finalizacion'),
  #          'release_asociado': ('Release Asociado'),
            'flujo_asociado': ('Flujo Asociado'),
        }

#------------------------------------------------------------------------------------
class consultar_sprint_form(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_creacion = forms.CharField(label='Fecha de Creacion',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_inicio = forms.CharField(label='Fecha de Inicio',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fecha_fin = forms.CharField(label='Fecha de Finalizacion',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #release_asociado = forms.CharField(label='Release Asociado',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    flujo_asociado = forms.CharField(label='Flujo Asociado',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = sprint
        fields = ('id','nombre','fecha_creacion', 'fecha_inicio', 'fecha_fin','release_asociado','flujo_asociado')
        
#    help_texts = {
#           'username': (''),
#      }
        

#------------------------------------------------------------------------------------
class buscar_sprint_form(forms.Form):
    BUSCAR_POR = {
                  ('id_sprint','ID Sprint'),
                  ('nombre','Nombre'),
                  ('flujo_asociado','Flujo Asociado')
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    
    busqueda = forms.CharField(widget=forms.TextInput())
