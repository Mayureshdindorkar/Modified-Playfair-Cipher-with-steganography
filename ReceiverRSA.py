# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:19:25 2021

@author: Piyush
"""
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

#Step 3: Decrypt cipher text using own private key. (To be run by receiver)

strprivatekey = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDCyMqq/b8MiYAMs2Zvn6vsnazRFLyLoSwa1CPIrwYiihPqmsff\nlT0N+ZtN84DY4stN7lcqwVLK2rWYzQzi5x0PHBYv09zrad/H+GFDw+FxplNNDmFQ\nZAjWhTk4pIAd7Km1PqxjCA1R1ohoiEd7Z/vMxNEG+EfbcakHnC9YMZCqUQIDAQAB\nAoGBALg038VZdwXKOzjHqEZEAHkinD6Wl8CMyYMNwFGXg/vCDRe/DOqa3kSLG55a\nfC2gPZgToIekkEGbGEXLFTa4TjdFocq1Y/oCMjFPEeee3WGcFFEuCB/URP+OeKAC\n38k3dsnYP8hz2j1UwEy3DBObtiSim3nbf5tf86uV0T/nOcVJAkEAyzprq+n4fLVj\n3Je/J13yYxMgl2kw4oFCk+kXGmhAm7OICiKH2xf2Ju7cU3JgA1slQriF+v1nFZb/\np4lh7UG8AwJBAPVdEOEZklJWURpgt1bHSO6u4/9xmgG0K+XHqElegQCyoRguFxHA\nimws0ZOfxXRujudiIdfv0+qZ8WFmnilN8hsCQQCAHD69q4tCChJ+f4Y3qchfXjJg\nYCY50uQGW5x9wBRiUoVCZkwf9/Xqyw5G6EXQN8fATJPhCZbPDFXy5e6+Yn7DAkEA\n7aelD8Lq/SFqEPiY3E7Oj5GKeQOZvgi7dCb9E4ObxAdBDeCmq6Uo7jpDDI/2ex4T\nAH8GdNdxFYziRgtVKoC6/QJAIHvp6P3u3FpPauw6p8s7MZpy9iY0pd1UTVVVgUI1\nUHC4lNLFsJghcHNoBsGmR91tM5Q2xhTbLKPrL/VEjFxOJA==\n-----END RSA PRIVATE KEY-----'
strciphertext = b'\x9f\x8a\x0b2c3z\x91H\xf0\xb2\xb7SlR\x9e\x1a\x12\xae\x05\x8eX\xce\x0b\x98u\xfa\xfe\x11\xe5\xcc\xac~\x12ZW\xeaM\xd9e\xdc7\xeeg\x90o\xd2 \x07\x1e\xe1\xea\xd1\t\\6;2\x8c\x16\xccl\x8c\x95\x1fC(dy7\x00\x94\xaa\xb0\xd9\x93\xb0\xce\x86K\x98\xeb\n\x930g\x95\x9bf|\xe0\x89\x07Iwmz:u\x83\xb2\n\xbfxsUK\x7fP\x92>\xb3\xc8O\x84\xde\xee\xed\x91Y\xba}\x82\xc0\xfb|K\x85'
pobj = RSA.importKey(strprivatekey)
pobj = PKCS1_OAEP.new(pobj)
print ("Decrypted message: ",pobj.decrypt(strciphertext))
"""
type('mayur'.encode('utf-8'))
Out[16]: bytes

ewe = 'mayur'.encode('utf-8')

type(ewe.decode())
Out[18]: str

"""