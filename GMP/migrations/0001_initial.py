# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('profile_photo', models.FileField(default=b'profile/profiledef.jpg', upload_to=b'profile/', verbose_name='Profile Photo', blank=True)),
                ('cover_photo', models.FileField(default=b'profile/coverdef.jpg', upload_to=b'profile/', verbose_name='Cover Photo', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
