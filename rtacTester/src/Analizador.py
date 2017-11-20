# -*- coding: utf-8 -*-
#!/usr/bin/python


import threading
import sys
import time
from datetime import datetime

class Regulador():
    def __init__(self):
        self.subregulador = 0
        self.inicializado = 0
        self.ahora = time.strftime("%c")
        
    def orden(self,msg):
        print "subreg 0 ->",
        sys.stdout.flush()
        parserHora(msg)
       # print "ahora %s" % (self.ahora),
        sys.stdout.flush()
        DetectoInicioCiclo(msg)
        DetectoInicioFase(msg)
        DetectoFinModoInicio(msg)
        print ""

def DetectoFinModoInicio(msg):
    if msg.find("Fin Modo Inicio") >= 0:
        print "Detecto Fin Modo Inicio"
        sys.stdout.flush()
    
    
def DetectoInicioCiclo(msg):
    if msg.find("Inicio de Ciclo") >= 0:
        print "Detecto Inicio de Cilco"
        sys.stdout.flush()



def DetectoInicioFase(msg):
    if msg.find("Inicio Fase") >= 0:
        print "Detecto Inicio de Fase"
        sys.stdout.flush()
        
        
          
def InicializacionCorrecta(msg):
    if msg.find("INICIALIZACION CORRECTA O.K") >= 0:
        print "DETECTADO FIN INICIALIZACION" 
        sys.stdout.flush()
        return True
    else:
        return False


def IsSubregulador(line):
    if line.find("Subregulador[0]") >= 0:
        return True
    else:
        return False

         
def parserHora(msg):
    dia = msg[1:9]
    hora = msg[10:18]
    
    #print "dia:%s" % (dia),
    #sys.stdout.flush()
        
    print "hora:%s" % (hora),
    sys.stdout.flush()


class Analizador():
    
    def __init__(self):
        self.accion = '='
        
    def update(self,msg):
        self.msg = msg
        
        print "up:%s" % (self.msg),
        sys.stdout.flush()
        
        if IsSubregulador(msg) == True:
            print "SUBREGULADOR 0" 
            sys.stdout.flush()
            self.accion = '6'
            
            
    def action(self):
        return self.accion



    
class Controlador(threading.Thread):
# Thread para lectura del pipe
    lck = threading.Lock()
    
    def __init__(self):
        threading.Thread.__init__(self)

        self.analizar = 0
        self.msg = ''
        self.orden = ''
        self.actuar = False
        self.analizador = Analizador()
        
    def run(self):
        while 1:
            print "up:%s" % (self.msg),
            sys.stdout.flush()
        
            if IsSubregulador(self.msg) == True:
                print "SUBREGULADOR 0" 
                sys.stdout.flush()
                self.orden = '6'

                

        
    def action(self):
        return self.orden

       
    def insert(self,msg):
        self.msg = msg
        print "w:%s" % (self.msg),
        sys.stdout.flush()

        
        

            
            
 