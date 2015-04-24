# -*- encoding: utf-8 -*-
"""
    Formularios
    ===========
    
    Módulo donde se especifícan los distintos formularios utilizados en la
    administración de B{L{Home<IS2_R09.apps.home>}}.

"""

from django import forms
from django.contrib.auth.models import User

class login_form(forms.Form):
    """
        Login
        =====
        
        Formulario destinado para la página de login del sistema.
        @cvar username: Campo donde el usuario especifíca su User Name al momento de logearse al sistema.
        @type username: CharField
        @cvar password: Campo donde el usuario especifíca su contraseña al momento de logearse al sistema.
        @type password: CharField
    """
    username= forms.CharField(widget=forms.TextInput())
    password= forms.CharField(widget=forms.PasswordInput(render_value=False))
    
class recuperar_contra(forms.Form):
    """
        Recuperación de contraseña
        ==========================
        
        Formulario destinado para la página de recuperción de contraseña del sistema.
        @cvar email: Campo donde el usuario especifíca su email solicitando la recuperación de contraseña.
        @type email: EmailField
        
    """
    email = forms.EmailField(label= "Email", widget= forms.TextInput())
    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            u = User.objects.get(email=mail)
        except User.DoesNotExist:
            raise forms.ValidationError('Email no registrado! Por favor ingrese un email correcto')
        return mail