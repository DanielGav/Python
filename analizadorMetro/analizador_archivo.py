#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


import datetime


class Itinerario:
    def __init__(self, itinerario, file_output):
        self.itinerario = itinerario
        self.inicio = False
        self.presencia = False
        self.aproximacion = False
        self.cancelacion = False
        self.fase = 0
        self.date_leido = datetime
        self.time_aprox = datetime
        self.time_presencia = datetime
        self.time_inicio = datetime
        self.time_cancelacion = datetime
        self.outfile = file_output


    def analisis_final(self):
        self.outfile.write("ANALISIS:")
        correcto = True

        if self.aproximacion == True:
            string_tmp = "Entrada por detector de aproximacion"
        elif self.presencia == True:
            string_tmp = "Entrada por detector de presencia"
        else:
            string_tmp = "Entrada no definida"
            correcto = False


        if self.inicio == False:
            string_tmp += " No detectado inicio de fase"
            correcto = False


        if self.cancelacion == True:
            string_tmp += " Detector de cancelacion detectado."


        if correcto == True:
            cadena = "[OK]" + string_tmp

        else:
            cadena = "[ERROR]" + string_tmp

        self.outfile.write(cadena)

    def detector_fin_itinerario(self,line):
        if line.find("VUELTA AL MODO NORMAL") >=0:

            string_tmp = self.print_cabecera() + " Fin itinerario"
            self.outfile.write(string_tmp)

            hora2 = self.get_hora(line)

            hora1 = self.time_inicio
            print("hora1", hora1)
            print("hora2", hora2)
            str_tiempo = hora2 - hora1
            print("str_tiempo:", str_tiempo)
            string_tmp = " Tiempo de fase de metro " + str(str_tiempo) + "\n"
            self.outfile.write(string_tmp)

            self.analisis_final()

            self.aproximacion = False
            self.cancelacion = False
            self.presencia = False
            self.inicio = False

            self.outfile.write("\n\n")

    def detector_aproximacion(self, line):
        if line.find("Activamos el detector de aproximacion por detector virtual") >=0:
            if self.aproximacion == False:
                self.aproximacion = True
                self.time_aprox = self.get_hora(line)
                string_tmp = self.print_cabecera() + " Detector de aproximacion\n"
                self.outfile.write(string_tmp)
        elif line.find("Activamos el detector de aproximacion") >= 0:
            if self.aproximacion == False:
                self.aproximacion = True
                self.time_aprox = self.get_hora(line)
                string_tmp = self.print_cabecera() + " Detector de aproximacion virtual\n"
                self.outfile.write(string_tmp)

    def detector_transicion_salida(self, line):
        if line.find("Transicion de salida de Fase") >=0:
            string_tmp = self.print_cabecera() + " Transicion salida\n"
            self.outfile.write(string_tmp)

    def detector_transicion_entrada(self, line):
        if line.find("Transicion de entrada de Fase") >=0:
            string_tmp = self.print_cabecera() + " Transicion entrada\n"
            self.outfile.write(string_tmp)

    def detector_presencia(self, line):
        if line.find("Activamos el detector de presencia") >=0:
            if self.presencia == False:
                self.presencia = True
                self.time_presencia = self.get_hora(line)
                string_tmp = self.print_cabecera() + " Detector de presencia\n"
                self.outfile.write(string_tmp)

    def detector_cancelacion(self, line):
        if line.find("Activamos el detector de cancelacion") >= 0:
            if self.cancelacion == False:
                self.cancelacion = True
                self.time_cancelacion = self.get_hora(line)
                string_tmp = self.print_cabecera() + " Detector de cancelacion\n"
                self.outfile.write(string_tmp)

    def detector_activado(self, line):
        self.detector_aproximacion(line)
        self.detector_presencia(line)
        self.detector_cancelacion(line)

    def detector_cruce_linea(self,line):
        if line.find("habilitamos el cambio de control de itinerario") >=0:
            string_tmp = self.print_cabecera() + " Cruce de linea\n"
            self.outfile.write(string_tmp)

    def detector_inicio_metro(self, line):
        if line.find("SACAMOS FASE DE METRO") >= 0:
            self.fase = 3
            self.time_inicio = self.get_hora(line)
            string_tmp = self.print_cabecera() + " Fase de Metro"
            self.outfile.write(string_tmp)
            self.inicio = True
            if self.aproximacion == True:
                hora1 = self.time_aprox
            else:
                hora1 = self.time_presencia

            hora2 = self.time_inicio

            str_tiempo = hora2 - hora1
            string_tmp = " Tiempo llegada " + str(str_tiempo) + "\n"
            self.outfile.write(string_tmp)

    def print_cabecera(self):
        return str(self.date_leido.time()) + ":Itinerario " + str(self.itinerario)

    def get_hora(self, line):
        subcadena = line[line.find('['):line.find(']')]
        subcadena = subcadena.strip()

        dia = subcadena[1:9]
        hora = subcadena[10:18]

        date_leido = datetime.datetime.strptime(dia, "%d/%m/%y")
        date_leido = datetime.datetime.strptime(hora, "%H:%M:%S")

        return date_leido

    def analizar(self, line):
        self.date_leido = self.get_hora(line)
        self.detector_activado(line)
        self.detector_transicion_entrada(line)
        self.detector_inicio_metro(line)
        self.detector_cruce_linea(line)
        self.detector_transicion_salida(line)
        self.detector_fin_itinerario(line)


class AnalizadorMetro:
    def __init__(self, regulador):
        self.regulador = regulador
        self.outfile = open('metro.txt', 'w')
        string_tmp = "Inicio analizador subregulador " + str(self.regulador) +"\n"
        self.outfile.write(string_tmp)
        self.itinerario_1 = Itinerario(1, self.outfile)
        self.itinerario_2 = Itinerario(2, self.outfile)

    def analizar(self, line):
        if line.find("Itinerario[1]") >= 0:
            self.itinerario_1.analizar(line)
        elif line.find("Itinerario[2]") >= 0:
            self.itinerario_2.analizar(line)

    def destructor(self):
        self.outfile.close()


def get_regulador(line):
    if line.find("Subregulador[0]") >= 0:
        return 1
    elif line.find("Subregulador[1]") >= 0:
        return 2
    elif line.find("Subregulador[2]") >= 0:
        return 3
    elif line.find("Subregulador[3]") >= 0:
        return 4
    else:
        return 0


def main():
    # En primer lugar debemos de abrir el fichero que vamos a leer.
    # Usa 'rb' en vez de 'r' si se trata de un fichero binario.
    infile = open('rtac.log', 'r')
    outfile = open('rtac_regulador0.txt', 'w') # Indicamos el valor 'w'.
    # Mostramos por pantalla lo que leemos desde el fichero
    print('>>> Lectura del fichero linea a linea')
    analizador = AnalizadorMetro(0)
    for line in infile:
        print(line)
        regulador = get_regulador(line)
        if regulador < 2:
            outfile.write(line)
            analizador.analizar(line)
        # Cerramos el fichero.
    infile.close()
    outfile.close()
    analizador.destructor()


if __name__ == '__main__':
    main()