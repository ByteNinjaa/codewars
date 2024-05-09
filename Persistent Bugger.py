#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

import math

def persistence(n):
    counter = 0
    while n >=10:
        product = 1
        while n > 0:
            digit = n % 10
            product *= digit
            n = math.floor(n/10)
        n = product
        counter += 1
    return counter
