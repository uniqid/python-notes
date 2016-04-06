# -*- coding: utf-8 -*-
__author__ = 'Jacky Yu <jacky325@qq.com>'

import sys, os, rsa, base64

#get current path
def get_cur_path():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(path)

def base64_encode(msg):
    return base64.b64encode(msg)

def base64_decode(msg):
    return base64.b64decode(msg)

#* encrypt message via pb.pem
#* generate pb.pem
#* openssl rsa -in pk.pem -RSAPublicKey_out -out pb.pem
def encrypt(msg, path = False):
    if path == False:
        path = get_cur_path() + '/cfg/pb.pem';

    try:
        with open(path) as pbfile:
            pubkey = rsa.PublicKey.load_pkcs1(pbfile.read())
        content = rsa.encrypt(msg, pubkey)
    except:
        return False
    else:
        return content

#* decrypt message which is encrypted by pb.pem via pk.pem
#* generate pk.pem
#* 1. openssl genrsa -des3 -out pk.pem 2048
#* 2. openssl rsa -in pk.pem -out pk.pem
def decrypt(msg, path = False):
    if path == False:
        path = get_cur_path() + '/cfg/pk.pem';

    try:
        with open(path) as pkfile:
            pkkey = rsa.PrivateKey.load_pkcs1(pkfile.read())
        content = rsa.decrypt(msg, pkkey)
    except:
        return False
    else:
        return content

#* sign message via pk.pem
def sign(msg, path = False):
    if path == False:
        path = get_cur_path() + '/cfg/pk.pem'

    try:
        with open(path) as pkfile:
            pkkey = rsa.PrivateKey.load_pkcs1(pkfile.read())
        signature = rsa.sign(msg, pkkey, 'SHA-1')
    except:
        return False
    else:
        return signature

#* verify singature
def verify(msg, signature, path = False):
    if path == False:
        path = get_cur_path() + '/cfg/pb.pem'

    try:
        with open(path) as pbfile:
            pubkey = rsa.PublicKey.load_pkcs1(pbfile.read())
        result = rsa.verify(msg, signature, pubkey)
    except:
        return False
    else:
        return result

# get content from file
def file_get_content(filepath):
    try:
        handle  = open(filepath)
        content = handle.read()
        handle.close()
    except:
        return False
    else:
        return content

#put content to file 
def file_put_content(filepath, content):
    try:
        handle = open(filepath, 'w+')
        handle.write(content)
        handle.close()
    except:
        return False
    else:
        return True
