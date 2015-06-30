<<<<<<< HEAD
psql -h localhost postgres -W -f scriptdb2.sql samuel

python manage.py syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'admin@example.com', 'root')" | ./manage.py shell
=======
psql -h localhost postgres -W -f scriptdb2.sql meliam

python manage.py syncdb

>>>>>>> 031471800e70d02fa2704ff1c9b796e9dde3af57
./manage.py runscript cusuario
./manage.py runscript crol
./manage.py runscript cflujo
./manage.py runscript cproyecto
<<<<<<< HEAD
./manage.py runscript csprint
./manage.py runscript cus
=======
>>>>>>> 031471800e70d02fa2704ff1c9b796e9dde3af57
