''' Questa parte del programma serve per comunicare
con Google Sheet
'''
import requests

SHEETY_ENDPOINT="Inserisci il tuo url"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    # Con questo metodoto leggiamo il foglio google dove sono registrate le nostre
    # preferenze di volo ed i costi
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # Questo metodo serve per scrivere sul foglio google il codice IATA
    def update_destination_data(self,row_idx):
        new_data = {
                "price":{
                "iataCode": self.destination_data[row_idx]["iataCode"]
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{self.destination_data[row_idx]['id']}", json=new_data)
        print(response.text)





