# Flight Finder

Questo programma è stato creato durante il corso online di 100 Days of Python ideato da 'The App Brewery'

Lo scopo del programma è quello di notificare l'utente ogni qual volta ci sia un volo in programma che costi meno della spesa previta dall'utente stesso. Il programma fa riverimento ad un foglio di lavoro google dove sono riportate le città di destinazione, il codice dell'aereoporto e la spesa massima che l'utente è disposto a spendere. La notifica avviene tramite l'invio di una mail all'utente. 

Questo programma prevede l'utilizzo della libreria 'smtplib' che permette di inviare email tramite python e di richieste API RESTful per comunicare sia con Google Sheet che con kiwi.com.

Per poter utilizzare questo programma bisogno prima creare un account per usuffriere delle API

In questo programma sono presenti 4 moduli oltre in main (il file principale):

- ### data_manager:
  Permette di comunicare con Google sheet
- ### flight_data:
  Permette di conservare i dati del volo in un oggetto
- ### flight_search:
  Permette di comunicare con il sito e di estrapolare le informazioni necessarie
- ### notification_manager:
  Permette di inviale una notifica quando si trovano voli che incontrano le nostre esigenze

## Struttura

Il programma si mette in moto ogni qual volta che lo facciamo partire. Una volta finita la ricerca dei voli presenti nel foglio google il programma smette di funzionare. Per una successiva ricerca va fatto ripartire. Se si vuole aggiungere altre destinazioni bisogna agire direttamente sul foglio google ed aggiornarlo.

Il programma è strutturato in questo modo

- ### main:
  Rappresenta il cuore del programma. Qui si importano i vari moduli e si comunica con il foglio google per vedere quali sono le destinazioni da noi desiderate. In questa perte si stabilisce anche l'aereoporto di partenza. Una volta caricati i dati presenti sul foglio google, la ricerca viene fatta tramite un ciclo for. Per ogni destiazione che rientra nei criteri stabiliti si invia una mail.
- ### data_manager:
  Permette di comunicare con Google sheet. In questo caso avrete bisogno dell'url del vostro foglio per poter leggere i dati. In questo modulo sono presenti due funzioni, 'get_destination_data' e 'update_destination_data'. La prima serve per leggere le varie destinazioni, mentre la seconda serve per poter fare una richiesta POST e inserire il codice dell'aereoporto qualora sia mancante.
- ### flight_data:
  Permette di conservare i dati del volo in un oggetto. Qui i parametri che costituiranno l'oggetto vanno inseriti, e si riferiscono al volo 'economico' che va bene per noi.
- ### flight_search:
  Permette di comunicare con il sito e di estrapolare le informazioni necessarie. Qui avremo bisogno di una API KEY che viene concessa nel momento in cui ci registriamo. Questa è una chiave personale e permette di indentificare chi sta cercando di accedere alle informazioni. Qui sono presenti due funzioni, 'get_destination_code' e 'check_flights'. La prima serve per prendere il codice dell'aereoporto, mentre la seconda è la funzione che ci permette di controllare fra i voli disponibili quale ci aggrada e di salvarne i dati
- ### notification_manager:
  Permette di inviale una notifica quando si trovano voli che incontrano le nostre esigenze. In questo modulo usiamo la libreria 'smtplib', qui avremo bisogno della nostra mail e di una password che google ci rilascia per far si che il programma possa accedere ed utilizzare il nostro account gmail. Ricorda, questa password è diversa dalla password che si usa per entrare in gmail. In questo modulo è presente la funzione 'send_mail' che è quella che ci permette di inviare la mail se troviamo un volo giusto per noi.
  
# Commenti

I commenti sono inseriti prima di un singolo blocco di codice per descrivere le funzionalità del codice e prima di variabili o azioni chiavi.
