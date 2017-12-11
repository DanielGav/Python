#!/usr/bin/python

import googlemaps
import requests
import json
import simplejson
import urllib
from datetime import datetime

#pip install requests

#file = open("testfile.txt","w")

#gmaps = googlemaps.Client(key='AIzaSyDLkWf0Lv5UU_au3SAEN3CFseehO1hG1vA')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
#                                     mode="transit",
#                                     departure_time=now)
#file.write("rsult: %s" %directions_result)

#file.close()

#origins=Washington,DC&destinations=New+York+City,NY

def main():

    home_coord = "Sevilla" # Home
    work_coord = "Mairena+del+Aljarafe,Sevilla" # Work
    api_key = "AIzaSyDLkWf0Lv5UU_au3SAEN3CFseehO1hG1vA"
    url_work = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + home_coord + "&destinations=" + work_coord + "&mode=driving&traffic_model=best_guess&departure_time=now&language=es&sensor=false&key=" + api_key
    result_work2home = simplejson.load(urllib.urlopen(url_work))

    driving_time_seconds_work2home = result_work2home['rows'][0]['elements'][0]['duration_in_traffic']['value']

    # Append results to the file
    driving_time_min = driving_time_seconds_work2home/60;
    result = datetime.now().strftime('%Y-%m-%d %H:%M') + ";" +work_coord+";"+ str(driving_time_min) + "mins\n"
    print(result)
    #target = open("Results.csv", 'a')
    #target.write(result)
    #target.close()

#    response = requests.get(url_work)

    # Get the response data as a python object.  Verify that it's a dictionary.
#    data = response.json()
#    print(type(data))
#    print(data)

if __name__ == '__main__':
  main()
