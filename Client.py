#Client
import socket
import os
import platform

host = socket.gethostname()
#Random port number
port = 12345

c = socket.socket()

#Connects to the server
c.connect((host, port))

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
	os.system('clear')
else:
	os.system('cls')
