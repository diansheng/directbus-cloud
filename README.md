### usefully scripts ###
```
rm -rf db/migrations
rm db.sqlite3
./manage.py makemigrations db
./manage.py migrate
./manage.py createsuperuser
./manage.py dumpdata db auth> fixture.json
./manage.py runserver
./manage.py loaddata fixture.json
```

### Superuser for admin ###
fremont/asdfqwer