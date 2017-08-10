# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 15:17
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sciper', models.PositiveIntegerField(blank=True, null=True)),
                ('where', models.CharField(blank=True, max_length=100, null=True)),
                ('units', models.CharField(blank=True, max_length=300, null=True)),
                ('group', models.CharField(blank=True, max_length=150, null=True)),
                ('classe', models.CharField(blank=True, max_length=100, null=True)),
                ('statut', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
