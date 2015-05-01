'''
Created on 30/4/2015

@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from django.forms.models import ModelForm
from IS2_R09.apps.Adjunto.models import adjunto
from django import forms

"""Muestra los formularios de Adjunto.
  adjunto_form: para creacion de adjuntos
  consultar_adjunto_form: para consulta de adjuntos
  modificar_adjunto_form: para modificacion de adjuntos
  eliminar_adjunto_form: para eliminacion de adjuntos ->no hay
"""

class adjunto_form(ModelForm):
    nombre = forms.CharField (widget=forms.TextInput(attrs={'class':'campos'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    version = forms.CharField(widget=forms.TextInput(attrs={'class': 'campos'}))
    comentario_commit = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    #archivo = forms.FileInput(required=False,widget=forms.FileInput(attrs={'class': 'archivo'}))

    class Meta:
        model = adjunto
        labels = {
            'nombre':('Nombre'),
            'descripcion':('Descripcion'),
            'version':('Version'),
            'comentario_commit': ('Comentario Commit'),
            #'archivo': ('Archivo'),
        }

#------------------------------------------------------------------------------------
class consultar_adjunto_form(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    descripcion = forms.CharField(label='Descripcion',widget=forms.Textarea(attrs={'readonly':'readonly'}))
    version = forms.CharField(label='Version',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    comentario_commit = forms.CharField(label='Comentario Commit',widget=forms.Textarea(attrs={'readonly':'readonly'}))
    #archivo = forms.FileInput(label='Archivo',widget=forms.FileInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = adjunto
        fields = ('id','nombre','descripcion', 'version', 'comentario_commit')#,'archivo')
        
#------------------------------------------------------------------------------------
#class eliminar_adjunto_form(forms.Form):

#-------------------------------------------------------------------------------------    
class modificar_adjunto_form(ModelForm):
    nombre = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'campos'}))
    descripcion = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'textarea'}))
    version = forms.CharField(label='Version',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    comentario_commit = forms.CharField(label='Comentario Commit',widget=forms.Textarea(attrs={'readonly':'readonly'}))
   # archivo =forms.FileInput(required=False,widget=forms.FileInput(attrs={'class': 'archivo'}))
    
    class Meta:
        model = adjunto
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class': 'campos'}),
                   'descripcion': forms.Textarea(attrs={'class': 'textarea'}),
                   'version' : forms.TextInput(attrs={'class' : 'campos'}),
                   'comentario_commit':forms.Textarea(attrs={'class':'textarea'}),
                   #'archivo' : forms.FileInput(attrs={'class': 'fileinput'}),
                   }
    