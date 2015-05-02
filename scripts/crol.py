from django.contrib.auth.models import Group

def run():
    g = Group.objects.create(name='Admin')
    g2 = Group.objects.create(name='Scrum')
    g3 = Group.objects.create(name='Developer')
    g2.save()
    g3.save()
    g.save()