import  requests
from pprint import pprint

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.ciudades = []
        self.SHETTY_URL = 'https://api.sheety.co/9a590837793e0e5497070ba9f027ef65/copiaDeFlightDeals/prices'
        self.header = {
            'Authorization': 'Bearer sdfsdfasdfsdf'
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

