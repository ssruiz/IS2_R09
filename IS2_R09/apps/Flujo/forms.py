# -*- encoding: utf-8 -*-
"""
    Formularios
    ===========
    
    Módulo donde se especifícan los distintos formularios utilizados en la
    administración de B{L{Flujos<IS2_R09.apps.Flujo>}}.

"""


from django.forms.models import ModelForm
from IS2_R09.apps.Flujo.models import flujo,actividad,kanban
from django import forms


class flujo_form(ModelForm):
    """
        Formulario Flujo
        ================
        
        Formulario usado en la creacion y modificación de B{Flujos}.
        Se obtiene a partir del L{modelo<IS2_R09.apps.Flujo.models.flujo>} de B{Flujo}.
    """
    class Meta:
        model = flujo
        exclude = ('user_stories',)
        widgets = {
                   'actividades': forms.CheckboxSelectMultiple()
                   }
        error_messages = {
            'actividades': {
                'required': ("El flujo debe tener al menos una actividad."),
                },
        }
class actividad_form(ModelForm):
    """
        Formulario Actividad
        ====================
        
        Formulario usado para la agregación de actividades a un B{Flujo}.
        Se obtiene a partir del L{modelo<IS2_R09.apps.Flujo.models.actividad>} de B{L{Flujo<IS2_R09.apps.Flujo>}}.
    """
    class Meta:
        model = actividad
        
class buscar_flujo_form(forms.Form):
    """
        Formulario de Búsqueda
        ======================
        
        Formulario usado para la búsqueda de un B{Flujo} por nombre.
        @cvar BUSCAR_POR: Lista de opciones por la que se orientará la búsqueda, en esta caso el nombre.
        @cvar opciones: Almacena la lista de opciones en un ChoiceFiedl.
        @type opciones: ChoiceField
        @cvar busqueda: Parametro o patrón a ser utilizado en la búsqueda.
        @type busqueda: Varchar 
    """
    BUSCAR_POR = {
                  ('nombre','Nombre'),
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR)
    busqueda = forms.CharField(widget=forms.TextInput())

class consultar_form(ModelForm):
    """
        Formulario de Consulta
        ======================
        
        Formulario usado en la consulta de B{Flujos}.
        Se obtiene a partir del L{modelo<IS2_R09.apps.Flujo.models.flujo>} de B{Flujo}
        al igual que L{flujo_form<IS2_R09.apps.Flujo.forms.flujo_form>}, sin embargo
        se modifican los campos haciendo que sean solo de lectura.
    """
    class Meta:
        model = flujo
        widgets = {
                   'actividades': forms.CheckboxSelectMultiple(attrs={'readonly':'readonly'}),
                   'nombre' : forms.TextInput(attrs={'readonly':'readonly'}),
                   }
class kanban_form(ModelForm):
    """
        Formulario kanban
        =================
        
        Formulario usado en la creacion y modificación de Kanban.
    """
    class Meta:
        model = kanban
        
class kanban_form_est(ModelForm):
    """
        Formulario kanban
        =================
        
        Formulario usado en la creacion y modificación de Kanban.
    """
    horas = forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = kanban
        