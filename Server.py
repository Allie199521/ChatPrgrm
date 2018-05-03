#Server
import Elgamal
from Crypto.Cipher import AES
import socket
from os import system 
import platform, random

host = socket.gethostname()
#Random port number
port = 12345

s = socket.socket()
#binds address and port
s.bind((host, port))

#listens in up to 2 connections at a time
s.listen(2)

#Accepts connection to the server
conn, addr = s.accept()

#Creates keys to be sent to Client once connected
p,a,g,ga = Elgamal.generateKey(8)

#places keys into a string format seperated by commas
publickeys = str(p) + "," + str(g) + "," + str(ga)

n = random.randint(10, 15)
key = ''

for i in range(0, n):
        key = key + str(random.randint(0, 9))
print(key)

#sends keys to client
conn.send(publickeys.encode())

#collecting public key from client
gb = conn.recv(1024).decode()

key = int(key)

print(str(Elgamal.encrypt(p, g, ga, key)))

conn.send(str(Elgamal.encrypt(p, g, ga, key)).encode())
#Prints out the address of who just got connected
print("Connection from: " + str(addr))

data = "1"

while data.lower().strip() != 'bye':
        # receive data stream. it won't accept data packet greater than 1024 bytes
    #
    data = conn.recv(1024).decode()
    #If no data is recieved, break
    if not data:
        break
    #Print what the client has sent
    print("client: " + str(data))
    data = input("You: ")
    #send the data to the client in bytes
    conn.send(data.encode())

#closes connection
conn.close()
pf = platform.system()

#if(pf == 'Linux' or pf == 'Darwin'):
#	system('clear')
#else:
#	system('cls')
