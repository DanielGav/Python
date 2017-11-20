#!/usr/bin/env python
#coding=utf-8

import subprocess
import threading
import re
import sys
 
from Analizador import *


# -- clases auxiliares --
class readpipe(threading.Thread):
    # Thread para lectura del pipe
    lck = threading.Lock()

    def __init__(self, pipe, callback=None):
        threading.Thread.__init__(self)
        self.pipe = pipe
        self.callback = callback

    def run(self):
        while 1:
            msg = self.pipe.readline()
            if not msg:
                break

            if self.callback:
                # bloquear, ejecutar funcion y desbloquear
                readpipe.lck.acquire()
                self.callback(msg)
                readpipe.lck.release()
                    
class writepipe(threading.Thread):
    # Thread para lectura del pipe
    lck = threading.Lock()

    def __init__(self, pipe, callback = None):
        threading.Thread.__init__(self)
        self.pipe = pipe
        self.callback = callback

    def run(self):
        while 1:
            
            msg = self.callback()
            if not msg:
                break
            
            if self.callback:
                # bloquear, ejecutar funcion y desbloquear
                writepipe.lck.acquire()
                self.pipe.write(msg)
                writepipe.lck.release()
        
def runapp(app, cbkStdOut = None, cbkStdErr = None, cbkStdIn = None, sh=False):

    # -- inicio --
    if not cbkStdErr:
        cbkStdErr = cbkStdOut

    if not sh:
        # la ejecucion CON shell precisa que app sea un str con el 
        # comando mas todos sus parametros
        # la ejecucion SIN shell precisa que app sea una lista 
        #[comando, parametro, parametro, ...]
        app = [p for p in re.split(" |(\".*?\")|(\'.*?\')", app) if p]

    try:
        pr = subprocess.Popen(app,
                                bufsize = 0,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE,
                                shell = sh)

    except  Exception, e:
        # fallo al ejecutar, comando incorrecto, ....
        raise

    # lanzar treads de captura
    #pr.communicate(input='1')
    tin = writepipe(pr.stdin,cbkStdIn)
    tout = readpipe(pr.stdout, cbkStdOut)
    terr = readpipe(pr.stderr, cbkStdErr)
    tout.start()
    terr.start()
    tin.start()
    # esperar que finalice
    pr.wait()

    # esperar que finalizen los threads,
    # en algunos casos se da el proceso por terminado pero todavia no se han cerrado
    # los pipes y quedan datos en los buffers, hay que esperar que los threads
    # terminen de capturar los datos
    while tout.isAlive() or terr.isAlive():
        pass

    # devolver codigo de salida de la aplicacion
    return pr.poll()


              

    


##############################
# rtAC Tester Main
##############################
if __name__ == "__main__":

    wk = Controlador()
    
    wk.start()

    def inputValue():
        return wk.action()
        
    def printstdout(msg):
        #print "c:%s" % (msg),
        #sys.stdout.flush()
        
        wk.insert(msg)

    def printstderr(msg):
        print "Err:%s" % (msg),
        sys.stdout.flush()
        

    def printlista(lista):
        for l in lista:
            print "\t%s" % l,

    # -- capturar resultado en tiempo real --
    cmd = "./rtac.out debug"
    ret =  runapp(cmd, printstdout, printstderr, inputValue)
    if ret == 0:
        print "%s OK " % cmd
    else:
        print "%s Falló con codigo %s" % (cmd, ret)
