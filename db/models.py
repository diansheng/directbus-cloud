from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Location(models.Model):
    latitude = models.DecimalField(blank=True, max_digits=9, decimal_places=6)  # South (-90, 90) North
    longitude = models.DecimalField(blank=True, max_digits=9, decimal_places=6)  # West (-180, 180) East
    street = models.CharField(max_length=100, blank=True)
    street_no = models.CharField(max_length=5, blank=True)
    post_code = models.IntegerField(max_length=6, blank=True)  # minimum length should also be 6


class Stop(models.Model):
    arrive_time = models.TimeField(null=True, blank=True)
    depart_time = models.TimeField(null=True, blank=True)
    stay_time = models.TimeField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)


class Route(models.Model):
    name = models.CharField(max_length=30, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    duration = models.TimeField(null=True, blank=True)
    stops = models.ManyToManyField(Stop)
    active = models.BooleanField(default=False)
    valid_start = models.DateTimeField(null=True, blank=True)
    expire = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=3, blank=True, null=True)

    def __unicode__(self):
        return str(self.user) or super(Route,self).__unicode__()

    def __str__(self):
        return str(self.user) or super(Route,self).__str__()


class Customer(models.Model):
    user = models.OneToOneField(User)
    mobile = models.IntegerField(max_length=10)
    route_subscribe = models.ManyToManyField(Route, related_name='subscribed_customers', blank=True)
    route_interest = models.ManyToManyField(Route, related_name='interested_customers', blank=True)
    # more fields including search_history, etc.

    def __unicode__(self):
        return str(self.user)

    def __str__(self):
        return str(self.user)


class Bus(models.Model):
    number_plate = models.CharField(max_length=10)
    capacity = models.IntegerField(max_length=3)  # todo: no max_length for integer field
    over_capacity = models.IntegerField(max_length=3, blank=True)

    class Meta:
        verbose_name_plural = "buses"


