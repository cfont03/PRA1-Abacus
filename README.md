# Repositori_Llibreria_Abacus_WebScraping

*Entre parèntesi s'indica el número de pregunta de la PRA1 que respon*

**(1)** El model de negoci tradicional ha experimentat un gran canvi en els darrers anys. En el seu moment i, encara avui dia, el petit negoci ha de fer front a les grans superfícies. Actualment, però, cal també afrontar la competència online. 
L'empresa "La llar del llibre" ha notat una forta baixada de ventes en llibres en els darrers 18 mesos. Durant aquest temps, de forma poc estructurada, l'empresa ha dut a terme diverses metodologies per tal de recuperar-ne les ventes: abaixar preus, incrementar la promoció online, millorar els temps d'entrega en la venta online, entre d'altres. 
Després de veure que aquestes no han sorgit quasi efecte, l'empresa ha decidit focalitzar-se en la seva competència més directe i més forta online, l'empresa Abacus Cooperativa, especialment després d'haver llegit la següent notícia: https://eshowmagazine.com/ultimas-noticias/abacus-incrementa-sus-ventas-online-un-245-en-2018/
Amb l'objectiu de recuperar-ne el mercat, l'empresa s'ha adreçat a dos estudiants de la Universitat Oberta de Catalunya per tal de fer una anàlisi sobre els llibres venuts online en la pàgina web de l'Abacus Coop. 

**(3)** És per això que l'objectiu d'aquesta primera pràctica és extreure la informació disponible sobre tots els llibres que es venen a través de la pàgina web de l'empresa Abacus Cooperativa (https://www.abacus.coop/es/libros), de manera automàtica. Conseqüentment, "La llar del llibre" podrà fer un seguiment constant i s'hi podrà ajustar de manera més precisa amb l'esperança de recuperar-ne les ventes perdudes. 

**(2)** És per tant que el dataset extret rebrà el títol de "Catàleg de llibres Abacus Coop."

**(5)** Les dimensions que s'extrauen sobre els llibres són les següents, en el mateix ordre, guardades en un arxiu CSV (excepte la Imatge, on es guardarà en una carpeta en el directori d'on s'executa el script). 
- Títol del llibre
- Autor del llibre
- ID de l'autor
- Editorial
- Preu de soci
- Preu de venta al públic (PVP)
- Tipus de producte
- Codi EAN
- Número de referència Abacus
- Enquadernació
- Col·lecció
- Matèria
- Ruta
- Imatge
- Data d'extracció

Tot i que la variable del preu pot semblar la més important per a "La llar del llibre", recomanem col·leccionar també les altres dimensions disponibles, ja que poden tenir una influència directe en el preu (per exemple, la disponibilitat, el tipus d'enquadernació o l'editorial). 
Aquestes variables seran vàlides només en el moment que s'executa el script. És per tant que també recomanem que aquest s'executi de manera periòdica, ja sigui quinzenalment o mensualment, per tal de fer un seguiment de l'evolució de la disponibilitat del catàleg i dels seus preus. 

Per tal d'executar el script en el llenguatge de programació Python, és necessari instal·lar les següents llibreries:

```
pip install pandas
pip install selenium
pip install chromedriver-py
```
Important: és necessari tenir instal·lat el "Chrome Driver" a la mateixa ruta des d'on s'executarà l'arxiu .py. 

A més a més, en executar el script, l'usuari té la oportunitat d'escollir dos paràmetres, si s'escau, separats per un tabulador:
- Paràmetre 1: L'usuari pot escollir entre les següents classificacions. En cas de no indicar-se, es descarregaran les dades a partir de la pàgina principal (https://www.abacus.coop/es/libros)
  - *top*: Llibres més venuts
  - *novetat*: Llibres en novetats
  - *comic*: Llibres de tipologia còmic
  - *viatge*: Llibres de tipologia viatge
  - *informatica*: Llibres de tipologia informàtica
  - *noficcio*: Llibres de tipologia No-ficció
- Paràmetre 2, número de pàgines: Variable numèrica. En cas de no indicar-se, es descarregaran les dades de totes les pàgines disponibles. 

**(7)** Amb aquest tipus d'anàlisis pretenem respondre a les següents preguntes i actuar conseqüentment:
- Evolució de preus (tant PVP com de socis) per llibre i al llarg del temps, la qual cosa permetrà al nostre client adaptar-ne els preus.
- Analitzar la diferència entre Preu PVP i de Soci i considerar la possibilitat d'aplicar un política semblant
- Conèixer quins llibres té l'Abacus Coop. en catàleg i oferir-los si s'escau
- Veure si l'editorial té una influència en el preu de venta
- Veure'n les ofertes puntuals, analitzar cada quan es llancen i quin dia de la setmana per tal d'establir una política d'ofertes dins "La llar del llibre"

**(4)** Per tal de veure'n una imatge representativa del resultat, veure DataSet.jpg

### Agraïments
**(6)** En primer lloc, agraïm a la família Fàbregues, propietaris de "La llar del llibre", la plena confiança concedida en nosaltres. Aquesta fe ens dona la oportunitat de posar en pràctica real els coneixements adquirits al llarg dels nostres estudis. Per part nostra, esperem haver assolit els objectius i requeriments plantejats per "La llar del llibre" amb total plenitud. 
En segon lloc, donar gràcies pel recolzament del professor col·laborador de la Universitat Oberta de Catalunya Sergio Trilles Oliver, per proporcionar-nos dels recursos necessaris per aprendre a fer "Web Scraping". 
Finalment, agrair el constant suport moral de les nostres famílies en el desenvolupament d'aquesta activitat. 

### Llicència
**(8)** El codi proporcionat així com les dades es publicarien sota la llicència Creative Commons Non-Commrcial i Share-Alike, també coneguda com CC BY-NC-SA 4.0, i que inclou les següents condicions:
- Es permet copiar, redistribuir, adaptar i modificar el material a través de qualsevol mitjà o format, així fomentant la col·laboració i filosofia "open-source".
- Per tal de promoure'n la col·laboració, queda garantit que qualsevol modificació o ús del material serà publicat sota la mateixa llicència, indicat sota el terme "Share Alike". 
- El material no pot ser emprat amb finalitats comercials i, per tant, l'àmbit es redueix purament a l'acadèmic, indicat sota el terme "Non Commercial". 

### Codificació
**(9)** Veure arxiu Abacus_Scraping.py

### Dataset
**(10)** El resultat del data set es troba publicat en dues fonts diferents:
- Github: Veure arxiu Abacus_Books.csv
- Zeonodo: 10.5281 / zenodo.4249668
  Font, Carlota y Dil, Jordi. (2020). Llibres Abacus (Versión v2.0) [Conjunto de datos]. Zenodo. Veure link https://doi.org/10.5281/zenodo.4249668

### Contribucions      
- Recerca prèvia:
  - Jordi Dil Giró
  - Carlota Font Castell
- Redacció de les respostes
  - Jordi Dil Giró
  - Carlota Font Castell
- Desenvolupament del codi
  - Jordi Dil Giró
  - Carlota Font Castell
- Desenvolupament del repositori
  - Jordi Dil Giró
  - Carlota Font Castell


**Treball realitzat pels estudiants Jordi Dil Giró i Carlota Font Castell**
