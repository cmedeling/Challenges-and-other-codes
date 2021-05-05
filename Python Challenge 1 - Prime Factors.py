# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:50:10 2021

@author: Carl-Michael
"""

def prime_factors(number):
    #print('works')
    factors = list()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    print(factors)
prime_factors(120)