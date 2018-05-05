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
p,a,g,ga = Elgamal.generateKey(64)

#places keys into a string format seperated by commas
publickeys = str(p) + "," + str(g) + "," + str(ga)

#sends keys to client
conn.send(publickeys.encode())

#collecting public key from client
gb = conn.recv(1024).decode()

#calculate gab
gab = pow(int(gb), a, p)

#turn key to string
key = gab.to_bytes(32, 'little')

#set IV
IV = 16 * '\x00'

#set mode
mode = AES.MODE_CBC

#set encrypt to new AES
encryption = AES.new(key, mode, IV=IV)
decryption = AES.new(key, mode, IV=IV)

#Prints out the address of who just got connected
print("Connection from: " + str(addr))

#set data to 1 so the while loop runs
data = '1'

while data.lower().strip() != 'bye':
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = decryption.decrypt(conn.recv(1024)).strip().decode()
    #If no data is recieved, break
    if not data:
        break
    #Print what the client has sent
    print("client: " + str(data))
    data = input("You: ")

    l = len(data)
    if l%16 != 0:
        data = data + ' '*(16-l%16)
    data = encryption.encrypt(data)

    #send the data to the client in bytes
    conn.send(data)

#closes connection
conn.close()
pf = platform.system()

#if(pf == 'Linux' or pf == 'Darwin'):
#	system('clear')
#else:
#	system('cls')
