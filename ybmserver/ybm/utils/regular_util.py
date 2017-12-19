#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

author = 'qiyue'

email_pattern = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
tel_phone_pattern = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"


def is_email(email):
    return re.match(email_pattern, email)


def is_tel_phone_number(phone_number):
    return re.match(tel_phone_pattern, str(phone_number))
