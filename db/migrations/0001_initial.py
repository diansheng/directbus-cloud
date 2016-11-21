# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 17:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(max_length=3)),
                ('over_capacity', models.IntegerField(blank=True, max_length=3)),
            ],
            options={
                'verbose_name_plural': 'buses',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('street_no', models.CharField(blank=True, max_length=5)),
                ('post_code', models.IntegerField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('distance', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrive_time', models.TimeField(blank=True, null=True)),
                ('depart_time', models.TimeField(blank=True, null=True)),
                ('stay_time', models.TimeField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db.Location')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(to='db.Stop'),
        ),
        migrations.AddField(
            model_name='customer',
            name='route_interest',
            field=models.ManyToManyField(related_name='interested_customers', to='db.Route'),
        ),
        migrations.AddField(
            model_name='customer',
            name='route_subscribe',
            field=models.ManyToManyField(related_name='subscribed_customers', to='db.Route'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
