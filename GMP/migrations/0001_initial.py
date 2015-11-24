# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Artist', max_length=20, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=20, verbose_name='Tittle')),
                ('text', models.CharField(max_length=80, verbose_name='Body')),
                ('link', models.URLField(verbose_name='Link')),
                ('picture', models.FileField(default=b'news/defnew.jpg', upload_to=b'news/', verbose_name='Photo', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('user', models.ForeignKey(related_name='ownerplaylist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL), max_length=20, verbose_name='Name')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('profile_photo', models.FileField(default=b'profile/profiledef.jpg', upload_to=b'profile/', verbose_name='Profile Photo', blank=True)),
                ('cover_photo', models.FileField(default=b'profile/coverdef.jpg', upload_to=b'profile/', verbose_name='Cover Photo', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=50, verbose_name='Tittle')),
                ('album', models.CharField(max_length=20, verbose_name='Album')),
                ('song', models.FileField(upload_to=b'songs/', verbose_name='Song')),
                ('author', models.ForeignKey(to='GMP.Artist')),
            ],
        ),
    ]
