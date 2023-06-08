# Questo modulo serve per comunicare le nofiche
# Fa uso della libreria smtplib
import smtplib

import requests

my_email="La tua mail"
password = "Password rilasciata da google per accedere al tuo account"

class NotificationManager:
    # Questo metodo permette di mandare le notifiche via mail
    def send_mail(self,my_message, email):
        #leggi da file exel ed estrapola i dati
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # transport layer security un modo per mantenere una connessione sicura tra me ed il server
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=my_message)



