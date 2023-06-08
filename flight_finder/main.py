'''
    Flight Finder
   Questo codice viene utilizzato per cercare voli
   ad un prezzo inferiore di quello che vorremmo pagare.
   Questo programma comunica con Google Sheet per vedere
   quali destinazioni sono di nostro gradimento per poi cercare
   l'offerta migliore.
   Questo codice è stato creato durante il corso 100 Days of Python
   ideato da The App Brewery.
   Versione di Vincenzo Bruno
   '''

# Importiamo i vari moduli che ci servono per comunicare con i server

from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests

# Comunichiamo con google sheet dove è presente
# nome della città, ITA code, Prezzo limitie che vogliamo pagare
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
SHEETY_ENDPONIT_GET="Il tuo url google sheet"

# Codice dell'aereoporto da cui partire
ORIGIN_CITY_IATA = "LON"
row_idx = 0

# Cerca la data di domani e quella fra sei mesi
# periodo di ricerca per i miei voli
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

flight_search = FlightSearch()
notification_manager = NotificationManager()

# Se non è presente inseriamo l'IATA code direttamnte con una richiesta API
for row in sheet_data:
    row_idx +=1
    if row["iataCode"] == "":
        from flight_search import FlightSearch
        flight_look = FlightSearch()
        row["iataCode"] = flight_look.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_data(row_idx-1)

# Per ogni destinazione inserita nel foglio google controlliamo i
# voli presenti ed i prezzi
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    #########Previene il blocco del codice se non ne trova##########
    if flight is None:
        continue

    # Se trova un volo che costi meno di quello stabilito
    # procede con l'inviare una notifica
    if flight.price < destination["lowestPrice"]:
        response = requests.get(url=SHEETY_ENDPONIT_GET)
        data_user = response.json()["users"]
        for name in data_user:
            print(name["firstname"])
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
            message = f'Subject:Low price alert!\n\nDear {name["firstname"]},\nOnly {flight.price} Euro ' \
                      f'to fly from {flight.origin_city}-{flight.origin_airport} ' \
                      f'to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} ' \
                      f'to {flight.return_date}.\n{link} '

            notification_manager.send_mail(message, name["email"])
