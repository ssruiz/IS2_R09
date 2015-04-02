from django.test import TestCase
from IS2_R09.apps.Usuario.models import usuario
from django.contrib.auth.models import User
import unittest 
# Create your tests here.
# Archivo de Test para el modelo Usuario, el cual extiende al User de Django

class test_content(TestCase):
    def setUp(self):
        # se inicializan tres User django, notar que al crear ya se asocia un Usuario al mismo
        u1= User.objects.create(username="plumber",password="asd",first_name="Samuel",last_name="Ruiz")
        u2= User.objects.create(username="box",password="qwer",first_name="Annie",last_name="Lee")
        u3 = User.objects.create(username="kios",password="asdf",first_name="Albert",last_name="Medrin")
        u4 = User.objects.create(username="time",password="rtt",first_name="Robert",last_name="Lee")
        
        
    # test que recupera los datos del user plumber le asigna un telefono y luego comprueba que la asignacion
    # se realizo      
    def test_user_usuario(self):
        usuario = User.objects.get(username = "plumber")
        usuario.usuario.telefono="444333"
        self.assertEqual(usuario.usuario.telefono, "444333")
        
    # test que recupera los datos del user kios. Esta vez se hace la la prueba comparando el codigo de su
    # usuario(exentension del modelo) correspondiente, que es 6 como se definio en setUp
    def test_user_usuario2(self):
        usuario = User.objects.get(username = "kios")
        self.assertEqual(usuario.usuario.user_id, 7)
    
    # test que recupera todos los user con apellido Lee
    # se controla que recupere 2 como se habian definifo en setUp
    def test_user_usuario3(self):
        usuario= User.objects.filter(last_name="Lee")
        i=0
        for u in usuario:
            i+=1 
        self.assertEqual(i,2)
       
    