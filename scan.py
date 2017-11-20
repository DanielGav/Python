 #!/usr/bin/env python
 # -*- coding: iso-8859-15 -*-
 #----------------------------------------------------------------------------
 # scan.py  Modulo para obtener una lista de los puertos series disponibles
 #----------------------------------------------------------------------------
 # Notas: En Linux solo se detectan los puertos del tipo /dev/ttySx 
 # disponibles, que son a los que la libreria pyserial les asigna los 
 # valores 0, 1, 2, etc.  Los dispositivos del tipo /dev/ttyUSBx no se
 # detectan. Para poder usarlos como cualquier otro dispositivo, se 
 # puede hacer un enlace simbolico:
 #   # ln -s /dev/ttyUSB0 /dev/ttyS10
 # Asociamos el dispositivo ttyUSB0 a uno del tipo ttyS10. En ese caso si 
 # se detecta correctamente con esta rutina. En este ejemplo devolveria el
 # valor 10 (si realmente en /dev/ttyUSB0 hay un conversor usb-serie)
 #----------------------------------------------------------------------------

 
import sys
import serial
 
 #-----------------------------------------------------------------------------
 # Buscar puertos series disposibles. 
 # ENTRADAS:
 #   -num_ports : Numero de puertos a escanear. Por defecto 20
 #   -verbose   : Modo verboso True/False. Si esta activado se va 
 #                imprimiendo todo lo que va ocurriendo
 # DEVUELVE: 
 #    Una lista con todos los puertos encontrados. Cada elemento de la lista
 #    es una tupla con el numero del puerto y el del dispositivo 
 #-----------------------------------------------------------------------------
def scan(num_ports ='COM5'):
    
    
     #-- Lista de los dispositivos serie. Inicialmente vacia
    dispositivos_serie = []
     
     #-- Escanear num_port posibles puertos serie
    for i in range(len(num_ports)):
        print "Escanenado %s puertos serie:" % num_ports[i]
        sys.stdout.write("puerto %s: " % num_ports[i])
        sys.stdout.flush()

        try:
        #-- Abrir puerto serie
            s = serial.Serial(num_ports[i],baudrate=9600)
         
            print "OK --> %s" % s.portstr
         
        #-- Si no hay errores, anadir el numero y nombre a la lista
            dispositivos_serie.append(num_ports[i])
         
        #-- Cerrar puerto
            s.close()
             
       #-- Si hay un error se ignora      
        except:
            print "NO"
        pass
         
     #-- Devolver la lista de los dispositivos serie encontrados    
    return dispositivos_serie
 
 
 #--------------------------
 # Pruebas del modulo Scan 
 #--------------------------
 #if __name__=='__main__':
 
   
   #-- Escanear los puertos.
   #-- Se puede indicar el numero de puertos a escaner
   #-- El modo "verbose" esta activado por defecto. Se desactiva con False

num_ports=['COM1','COM2','COM3','COM4','COM5','COM6']

puertos_disponibles=scan(num_ports)
   

