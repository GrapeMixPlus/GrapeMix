#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    def __unicode__(self):
        return self.user
    def create_user_profile(
        sender,
        instance,
        created,
        **kwargs
    ):
        if created:
            UserProfile.objects.create(user=instance)
            post_save.connect(create_user_profile, sender=User)

