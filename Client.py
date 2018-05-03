#Client
import socket
from os import system
import platform
import random
import Elgamal
from Crypto.Cipher import AES


host = socket.gethostname()
#Random port number
port = 12345

c = socket.socket()

#Connects to the server
c.connect((host, port))

#recieves public keys from Server
keys = c.recv(1024).decode()

#aes key from server
keys2 = c.recv(2048).decode()
print(keys2)

#splits the keys and places them into an array
pubkey = keys.split(",")

#Generate private key b with desired bit length
b = random.randint(1,8)
gb = pow(int(pubkey[1]),b) % int(pubkey[0])

#full mask sending to decrypt
gab = pow(int(pubkey[2], b))%int(pubkey[0])

#decrypting the AES key
keys2 = Elgamal.decrypt(pubkey[0], keys2, gab)
print(keys2)

#sending the public key of client to server
c.send(str(gb).encode())

#Collects input taken from the client
message = input("You: ")

#If the message submitted by the client is not "bye"
while message.lower().strip() != 'bye':
    #Change message into byte size and send to server
    c.send(message.encode())
    #collects the servers message and change it to a string
    data = c.recv(1024).decode()

    #Print on the terminal what the server has sent
    print('server: ' + data)

    #Prompts client again for input and assign message to the new input
    message = input("You: ")

#closes client connection
c.close()
pf = platform.system()

if(pf == 'Linux' or pf == 'Darwin'):
	system('clear')
else:
	system('cls')
