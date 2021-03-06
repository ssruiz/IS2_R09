# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from IS2_R09.apps.Usuario.models import usuario
from django.forms.models import ModelForm

class crear_usuario_form(forms.Form):
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput({'class': 'campos'}))
    apellido = forms.CharField(label="Apellido",widget=forms.TextInput({'class': 'campos'}))
    username = forms.CharField(label="User name",widget=forms.TextInput({'class': 'campos'}))
    email = forms.EmailField(label= "Email", widget= forms.TextInput({'class': 'campos'}))
    password_one = forms.CharField(label="PassWord", widget = forms.PasswordInput({'class': 'campos'},render_value=False))
    password_two = forms.CharField(label="Confirmar Password", widget= forms.PasswordInput({'class': 'campos'},render_value=False))
    def clean_username(self):
        usernam = self.cleaned_data['username']
        try:
            u = User.objects.get(username=usernam)
        except User.DoesNotExist:
            return usernam
        raise forms.ValidationError('Nombre de usuario ya existe')
    
    # funcion que comprube que el email del usuario a crear ya no este utilizado
    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            u = User.objects.get(email=mail)
        except User.DoesNotExist:
            return mail
        raise forms.ValidationError('Email ya registrado!')
    
    
    # funcion que comprueba que las contrasenhas ingresadas coincidan
    def clean_password_two(self):
        pass_one = self.cleaned_data['password_one']
        pass_two = self.cleaned_data['password_two']
        if pass_one == pass_two:
            pass
        else:
            raise forms.ValidationError('Passwords no coinciden')


    #foto_de_perfil = forms.ImageField(label = "FotoUsuario")
 
    # funcion que comprube que el username del usuario a crear ya no este utilizado
    
class usuario_form(ModelForm):
    first_name = forms.CharField(label="Nombre",widget=forms.TextInput({'class': 'campos'}))
    last_name = forms.CharField(label="Apellido",widget=forms.TextInput({'class': 'campos'}))
    username = forms.CharField(label="User name",widget=forms.TextInput({'class': 'campos'}))
    email = forms.EmailField(label= "Email", widget= forms.TextInput({'class': 'campos'}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        
        labels = {
            'first_name': ('Nombre'),
            'last_name': ('Apellido'),
        }
        help_texts = {
            'username': (''),
        }
        error_messages = {
            'username': {
                'required': ("Este campo es obligatorio."),
            },
        }
       
    
'''
    # funcion que comprueba que las contrasenhas ingresadas coincidan
    def clean_password_two(self):
        pass_one = self.cleaned_data['password']
        pass_two = self.cleaned_data['password_two']
        if pass_one == pass_two:
            pass
        else:
            raise forms.ValidationError('Passwords no coinciden')

'''

class extension_usuario_form(ModelForm):
    telefono = forms.CharField(label='Teléfono',widget=forms.TextInput({'class': 'campos'}),max_length=30, required=False)
    
    class Meta:
        model = usuario
        fields = ('telefono',)
        
#------------------------------------------------------------------------------------
class consultar_usuario_form(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    telefono = forms.CharField(label='Telefono',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')
        
    help_texts = {
            'username': (''),
        }
        

#------------------------------------------------------------------------------------
class buscar_usuario_form(forms.Form):
    BUSCAR_POR = {
                  ('username','Username'),
                  ('nombre','Nombre'),
                  ('apellido','Apellido')
                  }
    opciones = forms.ChoiceField(label='Buscar Por',required=True,widget=forms.Select(),choices=BUSCAR_POR,)
    
    busqueda = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese parámetro','title':'Parámetro de Búsqueda'}),error_messages={'invalid':'Debe ingresar '})
    
    def clean_busqueda(self):
        pass_one = self.cleaned_data['busqueda']
        if pass_one == '':
            raise forms.ValidationError('Ingrese un parámetro')
        else:
            print 'pase' 
            