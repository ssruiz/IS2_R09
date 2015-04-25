<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======
'''
Created on 24/4/2015

@author: meliam
'''
from django.test import TestCase
import unittest
from IS2_R09.apps.Sprint.models import sprint
#from django.contrib.auth.models import User
 
# Create your tests here.
class test_content(TestCase):
    def setUp(self):
        # se inicializan tres User django, notar que al crear ya se asocia un Usuario al mismo
        u = User.objects.create(username="plumber",password="asd",first_name="Samuel",last_name="Ruiz")
        p1= proyecto.objects.create(nombre="P1",descripcion="asd",cliente=u,fecha_creacion="2015-05-04")
        
        
    # test que recupera los datos del user plumber le asigna un telefono y luego comprueba que la asignacion
    # se realizo      
    def test_proyecto_nombre(self):
        proyect = proyecto.objects.get(nombre = "P1")
        print "Test 1. Imprimiendo nombre del Proyecto --> %s" %(proyect.nombre)
        
    def test_proyecto_cliente(self):
        proyect = proyecto.objects.get(nombre = "P1")
        print "Test 2. Imprimiendo nombre del Cliente de P1 --> %s" %(proyect.cliente)
>>>>>>> a5805a17db0ce9f5c91994702f7b4ae2c26bf5e0
