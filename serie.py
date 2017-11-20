#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
 
#----------------------------------------------------------------------------
# sg-eco1.py  Ejemplo de manejo del puerto serie desde python utilizando la
# libreria multiplataforma pyserial.py (http://pyserial.sf.net)
#
#  Se envia una cadena por el puerto serie y se muestra lo que se recibe
#
#  (C)2002 Chris Liechti (cliechti@gmx.net)
#  (C)2007 Juan Gonzalez
#
#  LICENCIA GPL
#----------------------------------------------------------------------------
 
import sys
import serial
import struct
 
#----------------------------------------------------------
#-- Abrir el puerto serie. Si hay algun error se termina
#----------------------------------------------------------
def enviar_trama(cadena):
    try:
        s = serial.Serial(puerto, velocidad)
        s.timeout=0;

        enviar=bytearray(cadena)

        for i in enviar:
            print("valor:%x",i)

            enviado=s.write(i)

        #-- Cerrar puerto serie
        s.close()
   
    except serial.SerialException:
        #-- Error al abrir el puerto serie
        sys.stderr.write("Error al abrir puerto (%s)\n" % str(puerto))
        sys.exit(1)
 

 

#-- Valor por defecto del puerto a usar
#-- Para que sea multiplataforma hay que emplear numeros entre 0 y 255
#-- Pero tambien se pueden usar cadenas ej. /dev/ttyUSB0 en Linux
puerto = 'COM5'
velocidad=2400
#-- Cadena de pruebas a enviar
cadena = [32,54]

enviar_trama(cadena)
print ("FIN")
