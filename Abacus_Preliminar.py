# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:18:45 2020

@author: jdil
"""


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


#Control del Temps
time_a = datetime.datetime.now().replace(microsecond=0)


dir_path = 'C:/Users/jdil/.spyder-py3/CODI/Imatges'

# Funció per agafar una URL d'una imatge y guardar-la en el directori definit
def imagen_descarga (url):    
    nombre = str (url.split ('/') [- 1])
    urllib.request.urlretrieve (url, os.path.join (dir_path, nombre))
    

#Set up the path to the chrome driver
PATH = "D:/Apps/Python36/CODI/chromedriver"
driver = webdriver.Chrome(PATH)

#Aqui definirem l'origen a rascar!
#driver.get("https://www.abacus.coop/es/libros")
driver.get("https://www.abacus.coop/es/libros/novedades-en-libros")

#Espero 2 segons a que carregui la pàgina
time.sleep(2)


### Tasca Inicial #####################
### Cal fer un clic al boto 'id="acccept-cookies"'

xpath1 =  "//*[@id='cookieConsent']/div/div[2]"

destination_page_link = driver.find_element_by_xpath(xpath1)
destination_page_link.click()


###################################################
# Obtinc el nombre de pàgines amb llibres
###################################################

# Dinàmicament cerco el nombre de pàgines:

driver.get("https://www.abacus.coop/es/libros/novedades-en-libros")
n_pagines = driver.find_element_by_xpath('//*[@id="product-search-results"]/div[2]/div[2]/div[13]/div/ul').get_attribute('data-count-pages')

n_pagines= str(n_pagines)


# Contenedor per totes les url als llibres
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
            
            #get the href property
            a = item.find_element_by_tag_name("h3").find_element_by_tag_name("a").get_property("href")
            
            # Append book's link to list of links
            #print('ref: ' + a)
            links.append(a)
            
        # Definim uns segons.. per evitar sobrecàrregues i simular un tarannà més humà
        # Caldria afegir un criteri d'aleatorietat
        
        time.sleep(1)
    except:
        print('Error al recuperar els links a les pàgines de cadascun dels lllibres')
        driver.close()
       
        
#Contenidor per construir el dataset amb tota la info dels llibres
all_details = []        
    
##################################################################################
#Funció per recuperar dinàmicament camps de la secció Fitxa Tècnica

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
##################################################################################


for llibre in links:
    
    driver.get(llibre) #llibre conte la URL!

    ################################################################
    #Obtenció dades a guardar per 1 llibre concret
    ################################################################
    
    #Definició de variables on es guardaran els valors a inserir
    
    t_ruta= ''    #Agrupació catalogada del llibre
    titol = ''    #Títol del llibre
    autor_id = '' #id_autor del llibre
    autor = ''    #Autor del llibre
    editorial = ''    #Editorial del llibre
    sinopsis = ''     #Sinopsis complerta
    preu_soci = ''    #Preu llibre soci
    preu_public = ''  #Preu públic
    
    # Elements fitxa tècnica
    tipus_producte = ''
    ean = ''
    ref_abacus = ''
    encuaderna = ''
    coleccio = ''
    materia = ''
        
    ################################################################
    # Ruta: Agrupació catalogada del llibre
    ################################################################
    
    rutes = driver.find_elements_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/ol/li')
    
    for element_ruta in rutes:  
        if (t_ruta == ''):
            t_ruta = element_ruta.text
        else:
            t_ruta = t_ruta + ' \ ' +  (element_ruta.text)
    
    
    ################################################################
    # Títol:
    ################################################################
    
    try:
        e_tit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h1')                                                                
        titol = e_tit.text.replace("\n","")
    except:
        titol=''
    
    ################################################################
    # Autor_Id:
    ################################################################

    try:    
        #e_autor_id = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h2[1]/a').get_property("href")
        
        
        e_autor_id = driver.find_element_by_xpath("//h2[@class='product-topinfo author']/a").get_property("href")
        
        autor_id = e_autor_id.replace("\n","").split ('/') [- 1]
    except:
        autor_id=''
    
    ################################################################
    # Autor:
    ################################################################
    
    try:              
        e_autor = driver.find_element_by_xpath("//h2[@class='product-topinfo author']/a")
        
        autor = e_autor.text.replace("\n","")
    except:
        autor =''
    
    ################################################################
    # Editorial:
    ################################################################
    
    try:
        #e_editorial = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[1]/h2[2]/a')       
        e_editorial = driver.find_element_by_xpath("//h2[@class='product-topinfo editorial']/a")                            
        editorial = e_editorial.text.replace("\n","")
    except:
        editorial=''
    
    ################################################################
    # Sinopsis:
    ################################################################
    
    try:
        titsin = driver.find_elements_by_xpath('//*[@id="description-and-detail"]/div[2]/div[1]')
        sinopsis = titsin[1].text
    except:
        sinopsis=''
    
    ################################################################
    # Elements Fitxa Tècnica:
    ################################################################
       
    
    try:
        ft1_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[1]/span[1]').get_attribute("innerHTML")
        ft1 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[1]/span[2]').get_attribute("innerHTML")
        asigna(ft1_pare, ft1)    
    except:    
        ft1_pare=''
        ft1=''
    
    try:
        ft2_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[2]/span[1]').get_attribute("innerHTML")
        ft2 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[2]/span[2]').get_attribute("innerHTML")
        asigna(ft2_pare, ft2)
    except:    
        ft2_pare=''
        ft2=''
    
    try:
        ft3_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[3]/span[1]').get_attribute("innerHTML")
        ft3 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[3]/span[2]').get_attribute("innerHTML")
        asigna(ft3_pare, ft3)
    except:    
        ft3_pare=''
        ft3=''
    
    try:
        ft4_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[4]/span[1]').get_attribute("innerHTML")
        ft4 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[4]/span[2]').get_attribute("innerHTML")
        asigna(ft4_pare, ft4)
    except:    
        ft4_pare=''
        ft4=''
    
    try:    
        ft5_pare = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[5]/span[1]').get_attribute("innerHTML")
        ft5 = driver.find_element_by_xpath('//*[@id="description-and-detail"]/div[2]/div[2]/div/div[5]/span[2]').get_attribute("innerHTML")
        asigna(ft5_pare, ft5)
    except:
        ft5_pare=''
        ft5=''
        
    
    #######################################
    # PREU DEL LLIBRE SOCIS
    #######################################
    
    try:
        e = driver.find_element_by_xpath("//*[@class='prices-add-to-cart-actions']/div[1]/div/div/div[1]/div/span/span[2]/span") #Valida
        preu_soci = e.text.replace("\n","") 
    except:
        preu_soci=''
    
    #######################################
    # PREU DEL LLIBRE Públic
    #######################################
    
    try:
        pe = driver.find_element_by_xpath("//*[@class='prices-add-to-cart-actions']/div[1]/div/div/div[2]/div/span/span[2]/span")
        preu_public =pe.text.replace("\n","") 
    except:
        preu_public = ''
        
    ################################################################
    #Imatge
    ################################################################
    
    try:
        link_imatge = driver.find_element_by_xpath("//*[@id='pdpCarousel-" + ref_abacus + "']/div[2]/div/img").get_property("src").split ('?') [0]
        imagen_descarga(link_imatge)
    except:
        print("//*[@id='pdpCarousel-" + ref_abacus + "']/div[2]/div/img")
   
    
    ###################################
    # MOSTRA VALORS
    ###################################
    
    
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
    
    time.sleep(1)

#FI BUCLE LLIBRES
    
# Emmagatzemo la informació en un CSV

df = pd.DataFrame(all_details)
df.to_csv("all_pages.csv",sep="¦")  #ASCII 221 (Separador emprat)


time_b = datetime.datetime.now().replace(microsecond=0)

print(time_b-time_a)

driver.close()