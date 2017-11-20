#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


import socket
import sys


def enviar(host, message):

        port = 6000

        my_socket = socket.socket()
        my_socket.connect((host,port))
        
        my_socket.send(message.encode())
                 
        print('Enviado virtual a ' + host + ' itinerario ' + message)
                 
        my_socket.close()


if __name__ == '__main__':

        if len(sys.argv) != 3:
                print('La cantidad de argumentos ingresada no es correcta')
        host = sys.argv[1]
        itinerario = sys.argv[2] 
        message = 'D1T'+itinerario
        enviar(host, message)
