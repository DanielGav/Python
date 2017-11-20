#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
 
#----------------------------------------------------------------------------
# Cliente TCP
#----------------------------------------------------------------------------

import socket, sys
 
def Enviar(host,message):

        port = 6000

        mySocket = socket.socket()
        mySocket.connect((host,port))
        
        mySocket.send(message.encode())
                 
        print ('Enviado virtual a '+host+' itinerario '+message)
                 
        mySocket.close()
 
if __name__ == '__main__':
        if len(sys.argv) != 3:
                print('La cantidad de argumentos ingresada no es correcta')
        host = sys.argv[1]
        itinerario = sys.argv[2] 
        message = 'D1T'+itinerario
        Enviar(host,message)
