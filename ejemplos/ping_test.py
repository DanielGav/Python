import os
import sys
import platform
import threading, subprocess
from datetime import datetime
 
 
class Hilo (threading.Thread):
    ping = "ping -c 1"
    def __init__(self,inicio,fin):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fin = fin
        if (platform.system()=="Windows"):
            self.ping = "ping -n 1"
        else :
            self.ping = "ping -c 1"
            
    def run(self,red):
        for subred in range(self.inicio,self.fin):
            direccion = red+str(subred)
            response = os.popen(self.ping+" "+direccion)
            for line in response.readlines():
                if ("ttl" in line.lower()):
                    print(direccion,"está activo")
                    break
                
class Application():
    num_hilos_max = 4
    
    
    def __init__(self):
        self.num_hilos_max = 4

    def run(self):
        ip = input("Ingresa la IP: ")
        ipDividida = ip.split('.')
         
        try:
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
            comienzo = int(input("Ingresa el número de comienzo de la subred: "))
            fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
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
                finAux = comienzo+self.num_hilos_max
                if(finAux > fin):
                    finAux = fin
                hilo = Hilo(comienzo, finAux)
                hilo.run(red)
                hilos.append(hilo)
                comienzo = finAux
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