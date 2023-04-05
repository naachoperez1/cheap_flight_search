import requests
import data_manager
import flight_search
from pprint import pprint
import datetime
import notification_manager

CIUDAD_SALIDA = 'LON'
CIUDADES_DESTINO = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
HOY = f"{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}" # 3/4/2023
SIX_MONTHS_FROM_TODAY = datetime.datetime.now() + datetime.timedelta(days=180)
FECHA_REGRESO = f"{SIX_MONTHS_FROM_TODAY.day}/{SIX_MONTHS_FROM_TODAY.month}/{SIX_MONTHS_FROM_TODAY.year}" # 30/9/2023

# NO PUEDO HACER MAS PETICIONES A LA API DE SHEETY POR ESO ESTE CODIGO NO FUNCIONA.
# data_ciudades = data_manager.DataManager()
# buscador_ciudades = flight_search.FlightSearch(data_ciudades.ciudades)
# iata_codes = buscador_ciudades.iata_code_getter()
# data_ciudades.edit_iata_codes(iata_codes)

buscador_ciudades = flight_search.FlightSearch(ciudades=CIUDADES_DESTINO, from_city=CIUDAD_SALIDA, precios=[1000,20,300,60,40,822,300,245,1000])
iata_codes = buscador_ciudades.iata_code_getter() # ['PAR','BER','TYO','SYD','IST','KUL','NYC','SFO','CPT']

vuelos = buscador_ciudades.search_to_city(to_cities=iata_codes, day_from=HOY, day_to=FECHA_REGRESO)
pprint(buscador_ciudades.vuelos)
mensaje = ''
for vuelo in buscador_ciudades.vuelos.keys():
    if len(buscador_ciudades.vuelos[vuelo])>1:
        mensaje += f"\n{vuelo}:\n {buscador_ciudades.vuelos[vuelo][1]}"


notification = notification_manager.NotificationManager(email_to=#### HERE GOES THE DESTINATION MAIL ####,message=mensaje)






