# -*- encoding: utf-8 -*-

from django.forms.models import ModelForm
from IS2_R09.apps.Proyecto.models import proyecto,Equipo
from django import forms


class proyecto_form(ModelForm):
    '''
        Formulario que usado en la creacion de proyectos
    '''
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_creacion =forms.DateField(widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_inicio =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_fin =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    descripcion = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = proyecto
        exclude = ['miembro',]
        labels = {
            'nombre': ('Nombre'),
            'descripcion': ('Descripcion'),
            'fecha_creacion':('Fecha Creación'),
            'fecha_inicio':('Fecha Inicio'),
            'fecha_fin':('Fecha Finalizacion'),
        }
        help_texts = {
            'miembro': ('Selecciona mas de uno presionando ctrl'),
            }
class equipo_form(ModelForm):
    class Meta:
        model = Equipo
        widgets = {
                   'proyect': forms.Select(attrs={'readonly': 'readonly'}),
                   }
        
class cantidad_form(forms.Form):
    cantidad = forms.CharField(widget=forms.TextInput(),help_text='Este campo es obligatorio',error_messages={'required':'Debe ingresar un numero',})

    def clean_cantidad(self):
        cant = self.cleaned_data['cantidad']
        cant2 = int(cant)
        if cant2 > 0:
            return cant
        elif cant2 <=0:
            raise forms.ValidationError('Debe introducir un numero mayor 0')

class modificar_form(ModelForm):
    fecha_creacion =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    fecha_inicio =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_fin =forms.DateField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    
    class Meta:
        model = proyecto
        exclude = ['miembro',]
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class': 'campos'}),
                   'fecha_creacion': forms.TextInput(attrs={'class': 'campos'}),
                   'fecha_inicio' : forms.TextInput(attrs={'class': 'campos'}),
                   'fecha_fin' : forms.TextInput(attrs={'class': 'campos'}),
                   'descripcion' : forms.Textarea(attrs={'class': 'textarea'}),
                   }

class consultar_form(ModelForm):
    class Meta:
        model = proyecto
        widgets = {
                   'nombre' : forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'fecha_creacion': forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'fecha_inicio' : forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'fecha_fin' : forms.TextInput(attrs={'readonly':'readonly','class': 'campos'}),
                   'descripcion' : forms.Textarea(attrs={'readonly':'readonly','class': 'textarea'}),
                   'miembro': forms.SelectMultiple(attrs={'readonly':'readonly'}),
                   }
class consulta_equipo_form(ModelForm):
    class Meta:
        model = Equipo

class buscar_proyecto_form(forms.Form):
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  ('cliente','Cliente')
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())