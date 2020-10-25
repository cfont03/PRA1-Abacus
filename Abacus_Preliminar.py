# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:18:45 2020

@author: jdil / cfont
"""

'''
    Importation of necessary libraries
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
import numpy as np
import re
import time

from bs4 import BeautifulSoup
import requests

import urllib
import os
import datetime
import randint


'''
    Preparation before scraping
'''

# Control del temps
time_a = datetime.datetime.now().replace(microsecond=0)

# Definició de la ruta d'on s'executa l'arxiu py
dir_root = os.path.dirname(os.path.abspath(__file__))
#dir_path = 'C:/Users/jdil/.spyder-py3/CODI/Imatges'

# Creació de la ruta on es guardaran les imatges
dir_path = os.path.join(dir_root, 'Imatges')
print(dir_path)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Funció per agafar una URL d'una imatge i guardar-la en el directori definit
def imagen_descarga (url):    
    nombre = str (url.split ('/') [- 1])
    urllib.request.urlretrieve (url, os.path.join (dir_path, nombre))

# Establimem del directori d'on s'executa l'arxiu .py al chrome driver
#PATH = "D:/Apps/Python36/CODI/chromedriver"
driver = webdriver.Chrome()

# Definició d'origen a rascar
driver.get("https://www.abacus.coop/es/libros/novedades-en-libros")

# Indicació que s'esperi entre un i dos segons a carregar la pàgina
time.sleep(randint(1,2))


'''
    Obtain ID of each book for web page's link
'''

# Acceptació de les cookies
xpath1 =  "//*[@id='cookieConsent']/div/div[2]"
destination_page_link = driver.find_element_by_xpath(xpath1)
destination_page_link.click()

# Comptar el número de pàgines
driver.get("https://www.abacus.coop/es/libros/novedades-en-libros")
n_pagines = driver.find_element_by_xpath('//*[@id="product-search-results"]/div[2]/div[2]/div[13]/div/ul').get_attribute('data-count-pages')
n_pagines= str(n_pagines)

# Definició d'una llista buida on s'hi guardaran els ID's de cada llibre per tal de crear un link per cadascún d'ells
links = []
for page in range(1,int(n_pagines)+1,1):      
    try:
        if page==1:            
            #driver.get("https://www.abacus.coop/es/libros")
            driver.get("https://www.abacus.coop/es/libros/novedades-en-libros")
        else:
            #driver.get("https://www.abacus.coop/es/libros?pageNo=" + str(page))     
            driver.get("https://www.abacus.coop/es/libros/novedades-en-libros/?pageNo=" + str(page))     
        incategory = driver.find_elements_by_class_name("product-tile-container")
        for i in range(len(incategory)):
            item = incategory[i]
            # Get the href property
            a = item.find_element_by_tag_name("h3").find_element_by_tag_name("a").get_property("href")
            # Append book's link to list of links
            #print('ref: ' + a)
            links.append(a) 
        # Definim que s'esperi entre 2 i 5 segons a canviar de pàgina per tal de simular un tarannà més humà
        time.sleep(randint(2,5))
    except:
        print('Error al recuperar els links a les pàgines de cadascun dels llibres')
        driver.close()
 

'''
    Extract each books' dimension, including images
    
'''
        
# Llista buida on es guardarà tota la informació relacionada amb els llibres
all_details = []        
    
# Funció per recuperar dinàmicament els camps de la secció "Fitxa Tècnica"
def asigna (etiqueta,valor):    
    global tipus_producte, ean, ref_abacus, encuaderna, coleccio, materia
    if (etiqueta == "Tipo de producto:" ):           
        tipus_producte = valor.replace("\n","")        
    elif (etiqueta == "EAN:"):           
        ean = valor.replace("\n","")        
    elif (etiqueta == 'Referencia Abacus:'):
        ref_abacus = valor.replace("\n","")        
    elif (etiqueta == 'Encuadernación:' or etiqueta == 'Encuadernació:'):
        encuaderna = valor.replace("\n","")        
    elif (etiqueta == 'Colección:' or etiqueta == 'Colecció:'):
        coleccio = valor.replace("\n","")        
    elif (etiqueta == 'Materia:' or etiqueta == 'Assignatura:'):
        materia = valor.replace("\n","")                

# Obtenció de les dades a guardar per cada llibre
for llibre in links:
    # Recuperem la URL
    driver.get(llibre)
    
    # Variables del llibre
    t_ruta= ''    # Agrupació catalogada del llibre
    titol = ''    # Títol del llibre
    autor_id = '' # id_autor del llibre
    autor = ''    # Autor del llibre
    editorial = ''    # Editorial del llibre
    sinopsis = ''     # Sinopsis completa
    preu_soci = ''    # Preu llibre soci
    preu_public = ''  # Preu públic (PVP)
    
    # Variables dels elements de la fitxa tècnica
    tipus_producte = ''
    ean = ''
    ref_abacus = ''
    encuaderna = ''
    coleccio = ''
    materia = ''
      
    # Ruta: Agrupació catalogada del llibre
    rutes = driver.find_elements_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/ol/li')
    
    for element_ruta in rutes:  
        if (t_ruta == ''):
            t_ruta = element_ruta.text
        else:
            t_ruta = t_ruta + ' \ ' +  (element_ruta.text)
    
    #### Obtenció de les variables del llibre
    # Títol:
    try:
        e_tit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h1')                                                                
        titol = e_tit.text.replace("\n","")
    except:
        titol=''
    
    # Autor_Id:
    try:    
        #e_autor_id = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h2[1]/a').get_property("href")
        e_autor_id = driver.find_element_by_xpath("//h2[@class='product-topinfo author']/a").get_property("href")
        autor_id = e_autor_id.replace("\n","").split ('/') [- 1]
    except:
        autor_id=''
    
    # Autor:
    try:              
        e_autor = driver.find_element_by_xpath("//h2[@class='product-topinfo author']/a")
        autor = e_autor.text.replace("\n","")
    except:
        autor =''

    # Editorial:
    try:
        #e_editorial = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h2[2]/a')       
        e_editorial = driver.find_element_by_xpath("//h2[@class='product-topinfo editorial']/a")                            
        editorial = e_editorial.text.replace("\n","")
    except:
        editorial=''

    # Sinopsis:
    try:
        titsin = driver.find_elements_by_xpath('//*[@id="description-and-detail"]/div[2]/div[1]')
        sinopsis = titsin[1].text
    except:
        sinopsis=''
    
    
    #### Variables dels elements de la fitxa tècnica
    # Tipus de producte
    try:
        ft1_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[1]/span[1]').get_attribute("innerHTML")
        ft1 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[1]/span[2]').get_attribute("innerHTML")
        asigna(ft1_pare, ft1)    
    except:    
        ft1_pare=''
        ft1=''
    
    # EAN
    try:
        ft2_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[2]/span[1]').get_attribute("innerHTML")
        ft2 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[2]/span[2]').get_attribute("innerHTML")
        asigna(ft2_pare, ft2)
    except:    
        ft2_pare=''
        ft2=''
    
    # Referència Abacus
    try:
        ft3_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[3]/span[1]').get_attribute("innerHTML")
        ft3 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[3]/span[2]').get_attribute("innerHTML")
        asigna(ft3_pare, ft3)
    except:    
        ft3_pare=''
        ft3=''
    
    # Encuadernació
    try:
        ft4_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[4]/span[1]').get_attribute("innerHTML")
        ft4 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[4]/span[2]').get_attribute("innerHTML")
        asigna(ft4_pare, ft4)
    except:    
        ft4_pare=''
        ft4=''
    
    # Col·lecció
    try:    
        ft5_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[5]/span[1]').get_attribute("innerHTML")
        ft5 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[5]/span[2]').get_attribute("innerHTML")
        asigna(ft5_pare, ft5)
    except:
        ft5_pare=''
        ft5=''
    
    # Preu socis
    try:
        e = driver.find_element_by_xpath("//*[@class='prices-add-to-cart-actions']/div[1]/div/div/div[1]/div/span/span[2]/span") #Valida
        preu_soci = e.text.replace("\n","") 
    except:
        preu_soci=''
    
    # Preu de venta al públic (PVP)
    try:
        pe = driver.find_element_by_xpath("//*[@class='prices-add-to-cart-actions']/div[1]/div/div/div[2]/div/span/span[2]/span")
        preu_public =pe.text.replace("\n","") 
    except:
        preu_public = ''
        
    # Imatge
    try:
        link_imatge = driver.find_element_by_xpath("//*[@id='pdpCarousel-" + ref_abacus + "']/div[2]/div/img").get_property("src").split ('?') [0]
        imagen_descarga(link_imatge)
    except:
        print("//*[@id='pdpCarousel-" + ref_abacus + "']/div[2]/div/img")
   
    
    # MOSTRA VALORS
    
    # print('t_ruta: ' + t_ruta)
    # print('titol: ' + titol)
    # print('autor_id: ' + autor_id)
    # print('autor: ' + autor)
    # print('editorial: ' + editorial)
    # print('sinopsis: ' + sinopsis)
    # print('preu_soci: '+ preu_soci)
    # print('preu_public: '+ preu_public)
    
    # # Elemtns fitxa tècnica
    # print('tipus_producte: '+ tipus_producte)
    # print('ean: '+ ean)
    # print('ref_abacus:', ref_abacus)
    # print('encuaderna: ' + encuaderna)
    # print('coleccio: '+ coleccio)


    # Definició diccionari base
    r = {
         "Titol": titol,
         "Autor": autor,
         "Autor_id": autor_id,         
         "Editorial": editorial,         
         "Preu_soci": preu_soci,
         "Preu_Public": preu_public,
         "Tipus_Producte": tipus_producte,
         "EAN": ean,
         "Ref_Abacus": ref_abacus,
         "Encuadernacio": encuaderna,
         "Coleccio": coleccio,    
         'Materia': materia,
         "Ruta": t_ruta
         #"Sinopsis": sinopsis
 		} 			
    all_details.append(r)
    time.sleep(randint(1,2))
  
# Emmagatzament de la informació en un CSV
df = pd.DataFrame(all_details)
df.to_csv("all_pages.csv",sep="¦")  #ASCII 221 (Separador emprat)

# Comprovació del temps necessitat
time_b = datetime.datetime.now().replace(microsecond=0)
print(time_b-time_a)

driver.close()
