import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, ciudades, from_city, precios):
        self.FROM_CITY = from_city
        self.ciudades = ciudades
        self.TEQUILA_URL = 'https://api.tequila.kiwi.com/locations/query'
        self.TEQUILA_APIKEY = {
            'apikey':# here goes your apikey
        }
        precios = [int(i) for i in precios]
        self.vuelos = {f'{self.FROM_CITY} - PAR': [precios[0]],
                       f'{self.FROM_CITY} - BER': [precios[1]],
                       f'{self.FROM_CITY} - TYO': [precios[2]],
                       f'{self.FROM_CITY} - SYD': [precios[3]],
                       f'{self.FROM_CITY} - IST': [precios[4]],
                       f'{self.FROM_CITY} - KUL': [precios[5]],
                       f'{self.FROM_CITY} - NYC': [precios[6]],
                       f'{self.FROM_CITY} - SFO': [precios[7]],
                       f'{self.FROM_CITY} - CPT': [precios[8]],}
    def iata_code_getter(self):
        #   Obtiene el codigo IATA para cada pais de la hoja de calculo
        #   y los devuelve en una lista. iata_codes =['PAR','BER','TYO','SYD','IST','KUL','NYC','SFO','CPT']
        iata_codes = []
        for ciudad in self.ciudades:
            parameters_tequila = {
                'term': f'{ciudad}',
                'location_type': 'city'
            }
            iata_code = requests.get(self.TEQUILA_URL, headers=self.TEQUILA_APIKEY, params=parameters_tequila).json()['locations'][0]['code']
            iata_codes.append(iata_code)
        return iata_codes

    def search_to_city(self, to_cities, day_from, day_to):
        #   Busca el vuelo mas barato desde FROM_CITY a cada ciudad de la lista 'to_cities', y los agrega a
        #   la propiedad self.vuelos de la clase.
        for city in to_cities:
            search_parametes = {
                'fly_from': f'{self.FROM_CITY}',
                'fly_to': f'{city}',
                'date_from':f'{day_from}',
                'date_to': f'{day_to}',
                'one_per_date': 1
            }
            vuelos_url = 'https://api.tequila.kiwi.com/v2/search'
            vuelos = requests.get(vuelos_url, headers=self.TEQUILA_APIKEY, params=search_parametes).json()
            for vuelo in vuelos['data'][:1]:
                precio = int(vuelo['price'])
                if precio < self.vuelos[f"{self.FROM_CITY} - {city}"][0]:
                    salida = vuelo['utc_departure'].split('T')[0]
                    llegada = vuelo['utc_arrival'].split('T')[0]
                    pasaje = f"Precio: ${precio}. Salida: {salida}. Llegada: {llegada}"
                    self.vuelos[f'{self.FROM_CITY} - {city}'].append(pasaje)


