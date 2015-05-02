'''
Created on 30/4/2015

@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from django.forms.models import ModelForm
from IS2_R09.apps.Adjunto.models import adjunto
from django import forms
from IS2_R09.apps.Comentario.models import comentario

"""Muestra los formularios de Adjunto.
  adjunto_form: para creacion de adjuntos
  consultar_adjunto_form: para consulta de adjuntos
  modificar_adjunto_form: para modificacion de adjuntos
  eliminar_adjunto_form: para eliminacion de adjuntos ->no hay
"""
class comentario_form(ModelForm):
    nombre= forms.CharField(widget=forms.TextInput(attrs={'class': 'campos'}))
    fecha_creacion = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    fecha_ultima_mod = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    comentario= forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model=comentario 

class comentario_consulta_form(ModelForm):
    nombre= forms.CharField(widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    fecha_creacion = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    fecha_ultima_mod = forms.DateField(widget=forms.TextInput(attrs={'class': 'campos','readonly':'readonly'}))
    comentario= forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea','readonly':'readonly'}))
    class Meta:
        model=comentario 