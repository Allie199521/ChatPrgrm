# Name: Sherilyn Tejada Martinez
# Course: CIS 475 - Intro to Cryptography
# Assignment: 4
# Date: 20 April 2018

import random
from fractions import gcd as ez_gcd
import math
import sympy as s

#generate both public and private keys with the current bit size
def generateKey(bit):
    a = random.randint(1,bit)
    b = random.randint(1,bit)
    p = random.getrandbits(bit)
    # makes sure p is a random generated prime
    if p % 2 == 0:
        p += 1
    while s.isprime(p)== False:
        p = random.getrandbits(bit)
        if p % 2 == 0:
            p += 1

    q = int((p - 1)/2)

    #makes sure the random generated g is a prime generator
    g = random.randint(1,p)
    while((g % p) == 0 or pow(g,2,p) == 0 or pow(g,q,p) == 0):
        g = random.randint(1,p)


    #Alice public half mask
    apub = pow(g,a, p)

    #Bob public half mask
    bpub = pow(g,b, p)

    key = open("keys.txt", "w")
    key.write("p = " + str(p) + "\n" + "a = " + str(a) + "\n" + "g^b = " + str(bpub))
    key.close()

    return p,a,g,apub


def encrypt(p,g,ga,key):
    #generate a random private key
    k = random.randint(1,p-1)
    beta = pow(g,k,p)
    alpha = key * pow(ga,k, p)
    print(alpha)
    return alpha%p

def decrypt(p,enkey,gab):
    # calulatethe inverse of the half mask
    neg_full = pulverizer(gab, p)
    # decrypt the message
    m = (enkey * neg_full) % p
    print(m)
    return m


# Makes sure the number generated is a prime
def isPrime (a):
    for i in range(2, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True

# Extended Euclidean algo
def pulverizer (e, phi):
    hold_phi = phi
    x, x2 = 1, 0
    y, y2 = 0, 1
    while phi:
        Q = e//phi
        x2, x = x - Q * x2, x2
        y2, y = y - Q * y2, y2
        e, phi = phi, e - Q * phi
    if x < 0:
        x += hold_phi

    return x
