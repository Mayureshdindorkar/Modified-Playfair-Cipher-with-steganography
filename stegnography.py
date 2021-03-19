# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:04:01 2021

@author: Piyush
"""
# documentation: https://domnit.org/blog/2007/02/stepic-explanation.html
# reference link_1: https://www.matec-conferences.org/articles/matecconf/pdf/2016/20/matecconf_icaet2016_02003.pdf

from stegano import lsb
secret = lsb.hide("1.png", "secret to be hidden")
secret.save("1_s.png")
clear_message = lsb.reveal("1_s.png")
print(clear_message)