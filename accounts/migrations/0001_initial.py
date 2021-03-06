# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-26 08:41
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, help_text='Your mobile number', max_length=100, null=True)),
                ('residence', models.CharField(blank=True, help_text='Where you live in', max_length=500, null=True)),
                ('website', models.URLField(blank=True, help_text='Your personal website', null=True)),
                ('microblog', models.CharField(blank=True, help_text='Your sina microblog', max_length=100, null=True)),
                ('qq', models.CharField(blank=True, help_text='Your QQ number', max_length=100, null=True)),
                ('wechat', models.CharField(blank=True, help_text='Your wechat id', max_length=100, null=True)),
                ('introduction', models.TextField(blank=True, help_text='Something about yourself', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
