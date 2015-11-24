# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(to='GMP.Song'),
        ),
        migrations.AddField(
            model_name='profile',
            name='lista',
            field=models.OneToOneField(related_name='lista', default=None, to='GMP.PlayList'),
        ),
    ]
