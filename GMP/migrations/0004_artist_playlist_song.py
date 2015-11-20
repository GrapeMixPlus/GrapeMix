# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0003_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=50, verbose_name='Tittle')),
                ('album', models.CharField(max_length=20, verbose_name='Album')),
                ('song', models.FileField(upload_to=b'multimedia/', verbose_name='Song')),
                ('author', models.ForeignKey(to='GMP.Artist')),
            ],
        ),
    ]
