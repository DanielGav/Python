#!/usr/bin/python

import simplejson
import urllib
import unicodedata
import csv, operator
from datetime import datetime

#pip install requests


def get_tiempo_recorrido(home, work):
    home_coord = str(home.strip())
    work_coord = str(work.strip())
    departure_time = "now"
    print "work_coord:%s" % work_coord
    api_key = "AIzaSyDLkWf0Lv5UU_au3SAEN3CFseehO1hG1vA"
    url_work = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + home_coord + "&destinations=" + work_coord + "&mode=driving&traffic_model=best_guess&departure_time=" + departure_time + "&language=es&sensor=false&key=" + api_key

    result_work2home = simplejson.load(urllib.urlopen(url_work))

    driving_time_seconds_work2home = result_work2home['rows'][0]['elements'][0]['duration_in_traffic']['value']

    # Append results to the file
    driving_time_min = driving_time_seconds_work2home/60;
    result = str(driving_time_min) + "mins\n"
    print(result)
    return str(driving_time_min)


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

    get_huelva()


if __name__ == '__main__':

    main()
