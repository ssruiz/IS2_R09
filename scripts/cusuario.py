from django.contrib.auth.models import User
def run():
    print 'soy un script'
    u = User.objects.create_user(username='Pablor',first_name='Pablo',last_name='Ramirez',email='em@is2.com',password='passwd')
    u.save()