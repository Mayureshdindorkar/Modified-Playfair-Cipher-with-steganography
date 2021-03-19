# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:23:44 2021

@author: Piyush
"""
# Step 1: To be run by receiver.
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def generate_keys():
   # key length must be a multiple of 256 and >= 1024
   key = RSA.generate(1024)
   publickey = key.publickey()
   return key.exportKey('PEM'), publickey.exportKey('PEM')


privatekey, publickey = generate_keys()

# print(type(publickey))

print("Public Key: ", publickey)

print("\n\nPrivate Key: ", privatekey)





"""
Public Key : b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC7P8EZKubkA2vrfmoEtEMDWgXY\nlQIovjRl8MR43dNZ4y3gE6t7RX5y/xNBLYMtGThmZ0jnOXiBTS1hA+fGylW/9O3F\n1HWDcfgl2PG/mORsnqwK+nZczGofWIY+oEROlf0cYihWNv+a0n/tDgaIhCDHtdrR\ndz4lhjBwMaHJT7zjKQIDAQAB\n-----END PUBLIC KEY-----'
"""