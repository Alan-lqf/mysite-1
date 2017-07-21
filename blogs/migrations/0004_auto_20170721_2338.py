# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-21 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20170721_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blognestedcomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blognestedcomment',
            name='blog_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.DeleteModel(
            name='BlogNestedComment',
        ),
    ]
