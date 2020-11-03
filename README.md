# Repositori_Llibreria_Abacus_WebScraping

*Entre parèntesi s'indica el número de pregunta de la Pràctica que respon*

(1) El model de negoci tradicional ha experimentat un gran canvi en els darrers anys. En el seu moment i, encara avui dia, el petit negoci ha de fer front a les grans superfícies. Actualment, però, cal també afrontar la competència online. 
L'empresa "La llar del llibre" ha notat una forta baixada de ventes en llibres en els darrers 18 mesos. Sense saber-ne el motiu exacte, una de les sospitoses raons és que el catàleg de llibres ofert és, en general, més car que la competència. Amb l'objectiu de recuperar-ne el mercat, l'empresa s'ha adreçat a dos estudiants de la UOC per tal de fer una anàlisi de la competència més directe, amb servei tant de venta a botiga com online: l'empresa Abacus Cooperativa. 

(3) És per això que l'objectiu d'aquesta primera pràctica és extreure la informació disponible sobre tots els llibres que es venen a través de la pàgina web de l'empresa Abacus Cooperativa (https://www.abacus.coop/es/libros), de manera automàtica. Conseqüentment, "La llar del llibre" podrà fer un seguiment constant i s'hi podrà ajustar de manera més precisa amb l'esperança de recuperar-ne les ventes perdudes. 

(5) Les dimensions que s'extrauen sobre els llibres són les següents, en el mateix ordre, guardades en un arxiu CSV (excepte la Imatge, on es guardarà en una carpeta en el directori d'on s'executa el script). 
- Títol del llibre
- Autor del llibre
- ID de l'autor
- Editorial
- Preu de soci
- Preu de venta al públic (PVP)
- Tipus de producte
- Codi EAN
- Número de referència Abacus
- Encuadernació
- Col·lecció
- Materia
- Ruta
- Imatge
- Data d'extracció

Tot i que la variable del preu és la més important per a "La llar del llibre", recomanem col·leccionar també les altres dimensions disponibles, ja que poden tenir una influència directe en el preu (per exemple, el tipus d'encuadernació o l'editorial). 
Aquestes variables seran vàlides només en el moment que s'executa el script. És per tant que també recomenem que aquest s'executi de manera periòdica, ja sigui quinzenalment o mensualment, per tal de fer un seguiment de l'evolució de la disponibilitat del catàleg i dels seus preus. 

Per tal d'executar el script en el llenguatge de programació Python, és necessari instal·lar les següents llibreries:

```
pip install pandas
pip install selenium
pip install chromedriver-py
```
Important: és necessari tenir instal·lat el "Chrome Driver" a la mateixa ruta des d'on s'executarà l'arxiu .py. 

## Agraïments
(6) 
## Llicència
(8) El codi proporcionat així com les dades es publicarien sota la llicència Creative Commons Non-Commrcial i Share-Alike, també coneguda com CC BY-NC-SA 4.0, i que inclou les següents condicions:
- El
