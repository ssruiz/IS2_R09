from django.contrib.auth.models import User
def run():
    print 'soy un script'
    u = User.objects.create_user(username='Pablor',first_name='Pablo',last_name='Ramirez',email='em@is2.com',password='passwd')
    u2 = User.objects.create_user(username='Luzm',first_name='Luz',last_name='Marecos',email='em2@is2.com',password='passwd2')
    u3 = User.objects.create_user(username='Pedron',first_name='Pedro',last_name='Niels',email='em3@is2.com',password='passwd')
    u4 = User.objects.create_user(username='Jes',first_name='Jessica',last_name='Gutierrez',email='em4@is2.com',password='passwd')
    u5 = User.objects.create_user(username='Joe',first_name='Joel',last_name='Salas',email='em5@is2.com',password='passwd')
    u6 = User.objects.create_user(username='Mari',first_name='Marilin',last_name='Salas',email='em6@is2.com',password='passwd')
    
    u.save()
    u2.save()
    u3.save()
    u4.save()
    u5.save()
    u6.save()