from django.contrib import admin
from .models import Location, Route, Customer, Stop, Bus
# Register your models here.

my_models = [Location, Route, Customer, Stop, Bus]

for m in my_models:
    admin.site.register(m)
