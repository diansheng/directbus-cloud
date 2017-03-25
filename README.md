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

#### TODO ####
1. home - CSS (frontend)
2. about - CMS (frontend)
3. current routes - CMS - retrieve from database (backend)
4. sign in/up/off - functions
5. user profile edit - http form post update
6. indicate your route - draw routes on google map, render using js, save in database
7. make payment - later - (backend)
8. view your tickets - later - (backend)