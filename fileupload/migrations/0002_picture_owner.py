# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
