#!/usr/bin/python3
# encoding: UTF-8
#
# Actualizador multiple
#


import os
import sys
import platform
import threading, subprocess
from datetime import datetime
 
class RemoteControl:
    __ping = "ping -c 1"
    def __init__(self,ip):
        if (platform.system()=="Windows"):
            self.__ping = "ping -n 1"
        else:
            self.__ping = "ping -c 1"
        self.ip=ip
    def ping(self):
        print("ping ",self.ip)
        response = os.popen(self.__ping+" "+self.ip)
        for line in response.readlines():
            if ("ttl" in line.lower()):
                return True
            else:
                return False
        
        
        
    
class Actualizador():
    __ping = "ping -c 1"
    red=""
    def __init__(self,inicio,fin,red):
        print("Inicializamos el actualizador")
        self.inicio = inicio
        self.fin = fin
        self.red=red
        if (platform.system()=="Windows"):
            self.__ping = "ping -n 1"
        else:
            self.__ping = "ping -c 1"
            
    def run(self):
        print("Ejecutando actualizador");
        for subred in range(self.inicio,self.fin):
            direccion = self.red+str(subred)
            remote_device=RemoteControl(direccion)
            if (remote_device.ping()) == True:
                print("OK")
                break
        
class Hilo (threading.Thread):
    def __init__(self,actualizador):
        threading.Thread.__init__(self)
        self.actualizador=actualizador
    def run(self):
        print("hilo creado");
        self.actualizador.run()
                
class Application():
    num_hilos_max = 4
    
    def __init__(self):
        self.num_hilos_max = 4

    def run(self):
        #ip = input("Ingresa la IP: ")
        ip = "192.168.0.1"
        ipDividida = ip.split('.')
         
        try:
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
            #comienzo = int(input("Ingresa el número de comienzo de la subred: "))
            comienzo=int(1)
            #fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
            fin=int(20)
        except:
            print("[!] Error")
            sys.exit(1)

        tiempoInicio = datetime.now()
        print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))
        NumeroIPs = fin-comienzo
        numeroHilos = int((NumeroIPs/self.num_hilos_max))
        hilos = []
        try:
            for i in range(numeroHilos):
                fin_tmp = comienzo+self.num_hilos_max
                if(fin_tmp > fin):
                    fin_tmp = fin
                actualizador = Actualizador(comienzo,fin_tmp,red)
                hilo = Hilo(actualizador)
                hilo.run()
                hilos.append(hilo)
                comienzo = fin_tmp
        except Exception as e:
            print("[!] Error creando hilos:",e)
            sys.exit(2)
         
        for hilo in hilos:
            hilo.join()
         
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio
        print("[*] El escaneo ha durado %s"%tiempo)

if __name__ == "__main__":
   app = Application()
   app.run()