# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from mongoengine import *

connect('test', host='120.25.240.242', port=27017, username='test', password='test')


class Blog(Document):
    author = StringField(max_length=20, min_length=1)
