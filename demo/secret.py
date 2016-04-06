#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Jacky Yu <jacky325@qq.com>'

import rsa, base64, uniqid.fun

data      = '\nInformation to be encrypted!\n'
encrypted = uniqid.fun.encrypt(data)
b64en     = uniqid.fun.base64_encode(encrypted)
b64de     = uniqid.fun.decrypt(uniqid.fun.base64_decode(b64en))

print b64en
print b64de

sign     = uniqid.fun.sign(data)
b64sign  = uniqid.fun.base64_encode(sign)
verified = uniqid.fun.verify(data, uniqid.fun.base64_decode(b64sign))

print b64sign
print verified
