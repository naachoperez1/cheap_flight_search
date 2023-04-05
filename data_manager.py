import  requests
from pprint import pprint

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.ciudades = []
        self.SHETTY_URL = # here goes your sheety google sheets url
        self.header = {
            'Authorization': # here goes your token
        }
        self.city_getter()


    def city_getter(self):
        # Obtiene el nombre de cada ciudad de la hoja de calculo.
        for i in range (9):
            peticion = requests.get(self.SHETTY_URL, headers=self.header).json()['prices'][i]['city']
            #pprint(peticion)
            self.ciudades.append(peticion)

    def edit_iata_codes(self, codes):
        # Escribe el codigo IATA para cada pais en la hoja de calculo. paris = PAR, berlin = BER, etc.
        pass

