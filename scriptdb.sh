psql -h localhost postgres -W -f scriptdb2.sql samuel

python manage.py syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'admin@example.com', 'root')" | ./manage.py shell
./manage.py runscript cusuario
./manage.py runscript crol
./manage.py runscript cflujo
./manage.py runscript cproyecto
./manage.py runscript csprint
./manage.py runscript cus
