import datetime
from django.test import TestCase
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto
from IS2_R09.apps.Usuario.models import Usuario
#from clientes.models import Cliente
from django.utils import timezone
from django.core.urlresolvers import reverse
#from IS2_R09.apps.Sprint.forms import SprintForm

# Create your tests here.

# models test
class SprintTest(TestCase):

    def crear_usuario(self, username='pruebaSprint', first_name= 'Prueba', last_name='Sprint Test', cedula='7545787', email='meli452@gmail.com',password='pruebasprint', is_superuser=False):
            return Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password, is_superuser=is_superuser)

 '''   def crear_cliente(self, username='cliente', first_name= 'mengano', last_name='test', cedula='4617', email='alfa.alvaro.rodriguez@gmail.com',password='alforro'):
            return Cliente.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password)


    def test_sprint_creation(self):
        cliente = self.crear_cliente()
        lider = self.crear_usuario()
        lider.save()
        proyecto= Proyecto.objects.create(nombre='ProyectoPrueba', lider_proyecto=lider, cliente=cliente, descripcion='Descripcion del proyecto de prueba' , fecha_creacion= datetime.date.today(), fecha_inicio=datetime.date.today(), fecha_fin=datetime.date.today(), estado='PEN', observaciones='esta es la observacion del test')
        s= Sprint.objects.create(nombre="PruebaTestSprint", proyecto=proyecto, descripcion="Pequenha descripcion para el test de Sprint", duracion_dias=12, observaciones= "no hay observaciones")
        self.assertTrue(isinstance(s, Sprint))
        self.assertEqual((s.__unicode__()), s.nombre)
'''