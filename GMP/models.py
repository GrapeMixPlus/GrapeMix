#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    name = models.CharField(u'Name', max_length=20)
    country = models.CharField(u'Country', max_length=20)
    city = models.CharField(u'City', max_length=50)
    facebook = models.URLField(u'Facebook', max_length=200)
    profile_photo = models.FileField(u'Profile Photo', upload_to='profile/', blank=True, default='profile/profiledef.jpg')
    cover_photo = models.FileField(u'Cover Photo', upload_to='profile/', blank=True, default='profile/coverdef.jpg')



