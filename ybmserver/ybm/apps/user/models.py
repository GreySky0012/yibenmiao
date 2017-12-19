# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=False, max_length=11)
