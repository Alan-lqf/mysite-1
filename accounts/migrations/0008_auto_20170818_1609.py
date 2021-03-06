# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 08:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20170818_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='follows',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.AddField(
            model_name='follow',
            name='fan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='star', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='star',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fan', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
