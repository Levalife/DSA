# -*- coding: utf-8 -*-

def gcd(a, b):
    if b > a:
        a, b = b, a
    while a - b > 0:
        a = a - b
    return a

def gcd(a, b):
    print(a, b)
    if a == 0:
        return b
    return gcd(b % a, a)

print(gcd(10, 15))
print(gcd(35, 10))
print(gcd(31, 2))