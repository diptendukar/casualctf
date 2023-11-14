#!/usr/local/bin/python

from Crypto.Util.number import *

p = getPrime(64)
q = getPrime(64)
n = p * q
e = 65537

flag = open('flag.txt', 'r').read()

assert GCD(e,(p-1)*(q-1)) == 1

ciphertext = []

for i in flag:
	ciphertext.append(pow(ord(i),e,n))



print("Modulus (N) = ",n)
print("Public exponent (e) = ",e)
print("Ciphertext (C) = ",ciphertext)
