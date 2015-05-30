psql -h localhost postgres -W -f scriptdb2.sql meliam

python manage.py syncdb

./manage.py runscript cusuario
./manage.py runscript crol
./manage.py runscript cflujo
./manage.py runscript cproyecto
