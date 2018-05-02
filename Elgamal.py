# Name: Sherilyn Tejada Martinez
# Course: CIS 475 - Intro to Cryptography
# Assignment: 4
# Date: 20 April 2018

import random
from fractions import gcd as ez_gcd
import math

#generate both public and private keys with the current bit size
def generateKey(bit):
    a = random.randint(1,bit)
    b = random.randint(1,bit)
    p = random.getrandbits(bit)
    # makes sure p is a random generated prime
    if p % 2 == 0:
        p += 1
    while isPrime(p)== False:
        p = random.getrandbits(bit)
        if p % 2 == 0:
            p += 1

    q = (p - 1)/2

    #makes sure the random generated g is a prime generator
    g = random.randint(1,p)
    while((g % p) == 0 or pow(g,2) % p == 0 or pow(g,q) % p == 0):
        g = random.randint(1,p)


    #Alice public half mask
    apub = pow(g,a) % p

    #Bob public half mask
    bpub = pow(g,b) % p

    key = open("keys.txt", "w")
    key.write("p = " + str(p) + "\n" + "a = " + str(a) + "\n" + "g^b = " + str(bpub))
    key.close()

    return p,a,g,apub


def encrypt(p,g,ga,letter,encrypt_txt):
    #change the letter into a number
    m = ord(letter)
    #generate a random private key
    k = random.randint(1,p-1)
    beta = pow(g,k) % p
    alpha = m * pow(ga,k)
    encrypt_txt.write(str(beta) + "," + str(alpha) + "\n")

def decrypt(p,a,decrypt_txt,read):
    for line in read:
        # split the cipher from the half mask
        point = line.split(",")
        gb = int(point[0])
        c = int(point[1])
        # calulate the fullmask
        full = pow(gb, a) % p
        # calulatethe inverse of the half mask
        neg_full = pulverizer(full, p)
        # decrypt the message
        m = (c * neg_full) % p
        decrypt_txt.write(chr(m))


# Makes sure the number generated is a prime
def isPrime (a):
    for i in range(2, int(math.sqrt(a)) + 1):
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

def main ():
    p,a,g,gb = generateKey(8)
    message = open("Assignment4_5.txt", "r")
    encrypt_txt = open("encrypt.txt","w")
    decrypt_txt = open("decrypt.txt", "w")
    for line in message:
        for letter in line:
            encrypt(p,g,gb,letter,encrypt_txt)

    encrypt_txt.close()
    read = open("encrypt.txt","r")
    decrypt(p,a,decrypt_txt,read)
    decrypt_txt.close()
    read.close()
    message.close()


main()
