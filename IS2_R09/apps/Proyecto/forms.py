from django.forms.models import ModelForm
from IS2_R09.apps.Proyecto.models import proyecto,Equipo
from django import forms



class proyecto_form(ModelForm):
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
            'fecha_creacion':('Fecha Creacion'),
            'fecha_inicio':('Fecha Inicio'),
            'fecha_fin':('Fecha Finalizacion'),
        }
        help_texts = {
            'miembro': ('Selecciona mas de uno presionando ctrl'),
            }
class equipo_form(ModelForm):
    class Meta:
        model = Equipo
    
class cantidad_form(forms.Form):
    cantidad = forms.CharField(widget=forms.TextInput(),required=True)