# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_id', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254)),
                ('contactno', models.CharField(max_length=10)),
            ],
        ),
    ]
