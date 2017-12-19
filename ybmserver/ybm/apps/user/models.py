# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserInfo(User):
    phone_number = models.CharField(blank=False, max_length=11)
