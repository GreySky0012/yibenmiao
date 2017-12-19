#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import rsa

author = 'qiyue'


def md5(origin_str):
    m = hashlib.md5()
    m.update(origin_str)
    return m.hexdigest()


def rsa_enc(message, private_key):
    return rsa.encrypt(message, private_key)


def rsa_dec(crypto, public_key):
    return rsa.decrypt(crypto, public_key)


def rsa_verify(message, sign, public_key):
    return rsa.verify(message, sign, public_key)
