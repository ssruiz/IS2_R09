from django import forms
from django.contrib.auth.models import User

class login_form(forms.Form):
    ''' Formulario para la la pagina de login del sistema.'''
    username= forms.CharField(widget=forms.TextInput())
    password= forms.CharField(widget=forms.PasswordInput(render_value=False))
    
class recuperar_contra(forms.Form):
    '''Formulario para la recuperacion de contrasenhas.'''
    email = forms.EmailField(label= "Email", widget= forms.TextInput())
    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            u = User.objects.get(email=mail)
        except User.DoesNotExist:
            raise forms.ValidationError('Email no registrado! Por favor ingrese un email correcto')
        return mail