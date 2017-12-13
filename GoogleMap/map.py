#!/usr/bin/python

import simplejson
import urllib
import unicodedata
import calendar
import csv, operator
import datetime
import time

#pip install requests

def calcular_fecha():
    #desde 1 enero 1970 00:00:00
    seg_una_hora = 3600
    seg_un_dia = seg_una_hora * 24
    seg_un_year = 365 * seg_un_dia

    seg_year = 37 * 31536000
    seg_year_bisiesto = 11 * 31622400
    seg_2018_utc = seg_year + seg_year_bisiesto

    cambio_horario_gmt = seg_una_hora

    seg_2018 = seg_2018_utc

    seg_2018_17_enero = seg_2018 + (17*seg_un_dia)

    seg_2018_17_enero_8am = seg_2018_17_enero + (8 * seg_una_hora )
    return seg_2018

def get_tiempo_recorrido(home, work):
    home_coord = str(home.strip())
    work_coord = str(work.strip())
    segundos = calcular_fecha()
    departure_time = str(segundos)
    print "work_coord:%s" % work_coord
    api_key = "AIzaSyDLkWf0Lv5UU_au3SAEN3CFseehO1hG1vA"
    url_work = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + home_coord + "&destinations=" + work_coord + "&mode=driving&traffic_model=pessimistic&departure_time=" + departure_time + "&language=es&sensor=false&key=" + api_key
    print "url_work:%s" % url_work
    result_work2home = simplejson.load(urllib.urlopen(url_work))

    driving_time_seconds_work2home = result_work2home['rows'][0]['elements'][0]['duration_in_traffic']['value']

    # Append results to the file
    driving_time_min = driving_time_seconds_work2home/60;
    result = str(driving_time_min) + "mins\n"
    print(result)
    return str(driving_time_min)


def get_test():

    home_coord = "Mairena+del+Aljarafe"

    direccion = "Sevilla"

    tiempo = get_tiempo_recorrido(home_coord, direccion)
    print "tiempo:%s" % tiempo


def get_centros_sevilla():

    csvfile = open("adultos_cadiz.csv", 'rb')
    entrada = csv.reader(csvfile, delimiter=';')

    target = open("ResultsAdultosCadiz.csv", 'a')
    salida = csv.writer(target, delimiter=';')

    home_coord = "San+Fernando"

    for reg in entrada:
        codigo = str(reg[0])
        codigo = codigo.strip()
        print "codigo:%s" % codigo

        numbre_centro = str(reg[2])
        nombre_centro_2 = numbre_centro.strip()

        direccion_leida= str(reg[4])
        direccion_2 = direccion_leida.strip()
        direccion_sin_tildes = direccion_2
        direccion_final = direccion_sin_tildes.replace(' ', '+')
        print "direccion:%s" % direccion_final

        provincia = str(reg[7])
        provincia_final = provincia.strip()
        print "provincia:%s" % provincia_final

        direccion = direccion_final + "," + provincia_final
        print "direccion:%s" % direccion

        tiempo = get_tiempo_recorrido(home_coord, direccion)
        print "tiempo:%s" % tiempo

        salida.writerow([codigo, nombre_centro_2, direccion_2, provincia_final, tiempo])

    csvfile.close()
    target.close()


def get_cadiz():

    csvfile = open("loc_cadiz.csv", 'rb')
    entrada = csv.reader(csvfile, delimiter=';')

    target = open("ResultsCadiz.csv", 'a')
    salida = csv.writer(target, delimiter=';')

    home_coord = "San+Fernando"

    for reg in entrada:
        codigo = str(reg[0])
        codigo = codigo.strip()
        print "codigo:%s" % codigo

        ciudad = str(reg[1])
        ciudad_2 = ciudad.strip()
        ciudad_sin_tildes = ciudad_2
        ciudad_final = ciudad_sin_tildes.replace(' ', '+')
        print "ciudad:%s" % ciudad_final

        provincia = str(reg[2])
        provincia_final = provincia.strip()
        print "provincia:%s" % provincia_final

        direccion = ciudad_final + "," + provincia_final
        print "direccion:%s" % direccion

        tiempo = get_tiempo_recorrido(home_coord, direccion)
        print "tiempo:%s" % tiempo

        salida.writerow([codigo, ciudad_2, provincia, tiempo])

    csvfile.close()
    target.close()

def get_sevilla():

    csvfile = open("loc_sevilla.csv", 'rb')
    entrada = csv.reader(csvfile, delimiter=';')

    target = open("ResultsSevilla.csv", 'a')
    salida = csv.writer(target, delimiter=';')

    home_coord = "Mairena+del+Aljarafe,Sevilla"

    for reg in entrada:
        codigo = str(reg[0])
        codigo = codigo.strip()
        print "codigo:%s" % codigo

        ciudad = str(reg[1])
        ciudad_2 = ciudad.strip()
        ciudad_sin_tildes = ciudad_2
        ciudad_final = ciudad_sin_tildes.replace(' ', '+')
        print "ciudad:%s" % ciudad_final

        provincia = str(reg[2])
        provincia_final = provincia.strip()
        print "provincia:%s" % provincia_final

        direccion = ciudad_final + "," + provincia_final
        print "direccion:%s" % direccion

        tiempo = get_tiempo_recorrido(home_coord, direccion)
        print "tiempo:%s" % tiempo

        salida.writerow([codigo, ciudad_2, provincia, tiempo])

    csvfile.close()
    target.close()


def get_huelva():

    csvfile = open("loc_huelva.csv", 'rb')
    entrada = csv.reader(csvfile, delimiter=';')

    target = open("ResultsHuelva.csv", 'a')
    salida = csv.writer(target, delimiter=';')

    home_coord = "Mairena+del+Aljarafe,Sevilla"

    for reg in entrada:
        codigo = str(reg[0])
        codigo = codigo.strip()
        print "codigo:%s" % codigo

        ciudad = str(reg[1])
        ciudad_2 = ciudad.strip()
        ciudad_sin_tildes = ciudad_2
        ciudad_final = ciudad_sin_tildes.replace(' ', '+')
        print "ciudad:%s" % ciudad_final

        provincia = str(reg[2])
        provincia_final = provincia.strip()
        print "provincia:%s" % provincia_final

        direccion = ciudad_final + "," + provincia_final
        print "direccion:%s" % direccion

        tiempo = get_tiempo_recorrido(home_coord, direccion)
        print "tiempo:%s" % tiempo

        salida.writerow([codigo, ciudad_2, provincia, tiempo])

    csvfile.close()
    target.close()



def main():
    get_centros_sevilla()
    #get_cadiz()
    #get_sevilla()


if __name__ == '__main__':

    main()
