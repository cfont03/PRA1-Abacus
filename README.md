# Repositori_Llibreria_Abacus_WebScraping

*Entre parèntesi s'indica el número de pregunta de la PRA1 que respon*

***(1)*** El model de negoci tradicional ha experimentat un gran canvi en els darrers anys. En el seu moment i, encara avui dia, el petit negoci ha de fer front a les grans superfícies. Actualment, però, cal també afrontar la competència online. 
L'empresa "La llar del llibre" ha notat una forta baixada de ventes en llibres en els darrers 18 mesos. Durant aquest temps, de forma poc estructurada, l'empresa ha dut a terme diverses metodologies per tal de recuperar-ne les ventes: abaixar preus, incrementar la promoció online, millorar els temps d'entrega en la venta online, entre d'altres. 
Després de veure que aquestes no han sorgit quasi efecte, l'empresa ha decidit focalitzar-se en la seva competència més directe i més forta online, l'empresa Abacus Cooperativa, especialment després d'haver llegit la següent notícia: https://eshowmagazine.com/ultimas-noticias/abacus-incrementa-sus-ventas-online-un-245-en-2018/
Amb l'objectiu de recuperar-ne el mercat, l'empresa s'ha adreçat a dos estudiants de la UOC per tal de fer una anàlisi sobre els llibres venuts online en la pàgina web de l'Abacus Coop. 

(3) És per això que l'objectiu d'aquesta primera pràctica és extreure la informació disponible sobre tots els llibres que es venen a través de la pàgina web de l'empresa Abacus Cooperativa (https://www.abacus.coop/es/libros), de manera automàtica. Conseqüentment, "La llar del llibre" podrà fer un seguiment constant i s'hi podrà ajustar de manera més precisa amb l'esperança de recuperar-ne les ventes perdudes. 

(2) És per tant que el dataset extret rebrà el títol de "Catàleg de llibres Abacus Coop."

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

Tot i que la variable del preu pot semblar la més important per a "La llar del llibre", recomanem col·leccionar també les altres dimensions disponibles, ja que poden tenir una influència directe en el preu (per exemple, la disponibilitat, el tipus d'encuadernació o l'editorial). 
Aquestes variables seran vàlides només en el moment que s'executa el script. És per tant que també recomanem que aquest s'executi de manera periòdica, ja sigui quinzenalment o mensualment, per tal de fer un seguiment de l'evolució de la disponibilitat del catàleg i dels seus preus. 

Per tal d'executar el script en el llenguatge de programació Python, és necessari instal·lar les següents llibreries:

```
pip install pandas
pip install selenium
pip install chromedriver-py
```
Important: és necessari tenir instal·lat el "Chrome Driver" a la mateixa ruta des d'on s'executarà l'arxiu .py. 

## Agraïments
(6) En primer lloc, agraïm 

## Llicència
(8) El codi proporcionat així com les dades es publicarien sota la llicència Creative Commons Non-Commrcial i Share-Alike, també coneguda com CC BY-NC-SA 4.0, i que inclou les següents condicions:
- Es permet copiar, redistribuir, adaptar i modificar el material a través de qualsevol mitjà o format, així fomentant la col·laboració i filosofia "open-source".
- Per tal de promoure'n la col·laboració, queda garantit que qualsevol modificació o ús del material serà publicat sota la mateixa llicència, indicat sota el terme "Share Alike". 
- El material no pot ser emprat amb finalitats comercials i, per tant, l'àmbit es redueix purament a l'acadèmic, indicat sota el terme "Non Commercial". 

## Codificació
(9) Veure arxiu Abacus.py

## Dataset
(10) 
