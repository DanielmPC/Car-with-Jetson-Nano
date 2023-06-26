'''import threading
from time import sleep

name = ''

def get_name():
    global name
    name = 'rogelio'

thread = threading.Thread(target=get_name)
thread.start()

while True:

    print(f"Hola {name}")
    sleep(2)

'''

from socket import *
from time import ctime
import threading
from time import sleep
import RPi.GPIO as GPIO
import comandos

data = ''
comandos.setup()

def get_command():
    
    while True:
        tcpCliSock, addr = tcpSerSock.accept()
        print(f"Connected from [ {addr} ]")
        dato = ''
        dato = tcpCliSock.recv(BUFSIZE).decode('ascii')
        sleep(0.1)
        global data
        data = dato

#road.setup()
HOST = '10.42.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

thread = threading.Thread(target=get_command)
thread.start()

try:
    while True:

        
        if data == 'D':
            comandos.derecha()
            
        if data == 'U':
            comandos.recto()
            
        if data == 'I':
            comandos.izquierda()
            
        if data == 'R':
            comandos.reversa()

        if data == 'S':
            comandos.paro()
        
        print(data)
        sleep(0.1)


except KeyboardInterrupt:
    #road.close()
    comandos.paro()
    GPIO.cleanup()
    tcpSerSock.close()