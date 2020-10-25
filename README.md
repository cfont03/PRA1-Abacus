# Repositori_Llibreria_Abacus_WebScraping
## Català

L'empresa "La llar del llibre" ha notat una forta baixada de ventes en llibres en els darrers 18 mesos. Sense saber-ne el motiu exacte, una de les sospitoses raons és que el catàleg de llibres ofert és, en general, més car que la competència. Amb l'objectiu de recuperar-ne el mercat, l'empresa s'ha adreçat a dos estudiants de la UOC per tal de fer una anàlisi de la competència més directe, amb servei tant de venta a botiga com online: l'empresa Abacus Cooperativa. 

És per axiò que l'objectiu d'aquesta primera pràctica és extreure la informació disponible sobre tots els llibres que es venen a través de la pàgina web de l'empresa Abacus Cooperativa (https://www.abacus.coop/es/libros), de manera automàtica. Consqüentment, "La llar del llibre" podrà fer un seguiment constant i s'hi podran ajustar de manera més precisa amb l'esperança de recuperar-ne les ventes perdudes. 

Les dimensions que s'extrauen sobre els llibres són les següents, en el mateix ordre, guardades en un arxiu CSV (excepte la Imatge, on es guardarà en una carpeta en el directori d'on s'executa el script). 
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

Tot i que la variable del preu és la més important per a "La llar del llibre", recomanem col·leccionar també les altres dimensions disponibles, ja que poden tenir una influència directe en el preu (per exemple, el tipus d'encuadernació o l'editorial). 
Aquestes variables seran vàlides només en el moment que s'executa el script. És per tant que també recomenem que aquest s'executi de manera periòdica, ja sigui quinzenalment o mensualment, per tal de fer un seguiment de l'evolució de la disponibilitat del catàleg i dels seus preus. 

Per tal d'executar el script en el llenguatge de programació Python, és necessari instal·lar les següents llibreries:

```
pip install pandas
pip install selenium
pip install chromedriver-py
```
Important: és necessari tenir instal·lat el "Chrome Driver" a la mateixa ruta des d'on s'executarà l'arxiu .py. 


Agraïments:
