from django.test import TestCase
import unittest
from IS2_R09.apps.Comentario.models import comentario
from django.contrib.auth.models import User
import datetime 
# Create your tests here.
class test_content(TestCase):
    def setUp(self):
        c = comentario.objects.create(nombre='comentario',comentario='Se realizaron cambios en codigo.py',fecha_creacion=datetime.date.today(),fecha_ultima_mod=datetime.date.today())
        c = comentario.objects.create(nombre='comentario2',comentario='Se realizaron cambios en codigo2.py',fecha_creacion=datetime.date.today(),fecha_ultima_mod=datetime.date.today())
        
        
    def test_coment_nombre(self):
        coment = comentario.objects.get(nombre = "comentario")
        print "Test 1. Imprimiendo nombre del comentario --> %s" %(coment.nombre)
        
    def test_coment_fecha(self):
        coment = comentario.objects.filter(fecha_creacion = datetime.date.today())
        for c in coment:
            print "Test 2. Imprimiendo nombre del comentario --> %s" %(c.nombre)
    