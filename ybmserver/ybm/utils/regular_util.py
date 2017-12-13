#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

author = 'qiyue'

email_pattern = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"


def is_email(email):
    return re.match(email_pattern, email)
