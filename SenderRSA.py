# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:54:55 2021

@author: Piyush
"""
#Step 2: Get Public Key of Receiver for encrypting the plain text. (To be run by sender)
    
        
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



strpublickey = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCyMqq/b8MiYAMs2Zvn6vsnazR\nFLyLoSwa1CPIrwYiihPqmsfflT0N+ZtN84DY4stN7lcqwVLK2rWYzQzi5x0PHBYv\n09zrad/H+GFDw+FxplNNDmFQZAjWhTk4pIAd7Km1PqxjCA1R1ohoiEd7Z/vMxNEG\n+EfbcakHnC9YMZCqUQIDAQAB\n-----END PUBLIC KEY-----'
pobj = RSA.importKey(strpublickey)
pobj = PKCS1_OAEP.new(pobj)
print(pobj.encrypt(b'You can attack now!'))



# print(pk.encrypt("Hello", 12) == importedpk.encrypt("Hello", 12))