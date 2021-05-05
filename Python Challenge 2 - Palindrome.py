# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:09:33 2021

@author: Carl-Michael
"""

def palindrome(inputstring):
    forward = inputstring.replace(' ', '').replace("'", '').replace('-', '').lower()
    backward = forward[::-1]
    if backward == forward:
        print('True')
    else:
        print("False")
    #pass

palindrome("Go hang a salami - I'm a lasagna hog")
