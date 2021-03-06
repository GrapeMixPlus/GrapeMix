#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    name = models.CharField(u'Name', max_length=20, default=user)
    country = models.CharField(u'Country', max_length=20)
    city = models.CharField(u'City', max_length=50)
    facebook = models.URLField(u'Facebook', max_length=200)
    profile_photo = models.FileField(u'Profile Photo', upload_to='profile/', blank=True, default='profile/profiledef.jpg')
    cover_photo = models.FileField(u'Cover Photo', upload_to='profile/', blank=True, default='profile/coverdef.jpg')

    def __str__(self):
		return self.name

class Artist(models.Model):
    name = models.CharField(u'Name', max_length=20, default="Artist")

    def __str__(self):
        return self.name

class Song(models.Model):
    tittle = models.CharField(u'Title', max_length=50)
    author = models.CharField(u'Author', max_length=50)
    album = models.CharField(u'Album', max_length=20)
    song = models.FileField(u'Song', upload_to='songs/', blank=False)

    def __str__(self):
		return self.tittle


class PlayList(models.Model):
    name = models.CharField(u'Name', max_length=20)
    song = models.ManyToManyField(Song)
    user = models.ForeignKey(User, related_name='ownerplaylist',default=None)

    def __str__(self):
		return self.name

class New(models.Model):
    class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"
		#ordering=['-fecha']
    titulo = models.CharField(u'Tittle', max_length=20)
    #fecha = models.DateTimeField(u'Fecha New',auto_now_add=True)
    text = models.CharField(u'Body', max_length=80)
    link = models.URLField(u'Link', max_length=200)
    picture = models.FileField(u'Photo', upload_to='news/', blank=True, default='news/defnew.jpg')

    def __str__(self):
		return self.titulo
