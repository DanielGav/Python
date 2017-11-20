#!/bin/bash
#
#Codigo de ejecutor para Code::block

# OPCIONES DEFINIDAS
# ejecutar.sh [-d]
# opcion:
# -d: (NO OBLIGATORIO) PONE MODO DEBUG
# ejemplo: ejecutar.sh -d



#MAQUINA="10.15.45.11"
MAQUINA="192.168.4.190"
#MAQUINA="172.16.11.114"
#MAQUINA="10.15.44.12"


USER="root"

#PASS="pisa14"
#PASS="cartuja93"
PASS="exposicion34"


RUTA_REMOTA="/home/rtgen7/"
RUTA_LOCAL="test.py"

#Comenrat MODO si no queremos usar la autocopìa

clear


if (ping -c 1 $MAQUINA|grep "errors")> /dev/null
then
	echo "ERROR DESTINO NO ACCESIBLE"

else
	echo "PARAMOS Y ELIMINAMOS"
	sshpass -p $PASS ssh $USER@$MAQUINA "killall rtac.out;killall python"
	
	RUTA_LOCAL="test.py"
	echo "COMPIAMOS EL EJECUTABLE $RUTA_LOCAL A LA MAQUINA REMOTA $MAQUINA"
	sshpass -p $PASS scp $RUTA_LOCAL $USER@$MAQUINA:$RUTA_REMOTA
	RUTA_LOCAL="Analizador.py"
	echo "COMPIAMOS EL EJECUTABLE $RUTA_LOCAL A LA MAQUINA REMOTA $MAQUINA"
	sshpass -p $PASS scp $RUTA_LOCAL $USER@$MAQUINA:$RUTA_REMOTA
fi
echo "HECHO"




