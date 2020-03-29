# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib3
import requests
#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pandas as pd  
import re
import os
import ssl

#página onde são listados todos os concursos
url_concursos = "https://www.concursosfcc.com.br/concursoOutraSituacao.html"

#baixando a página
#desabilita avisos de erro de certificado ssl
urllib3.disable_warnings()
#faz request na página, ignorando o certificado SSL
req = requests.get(url_concursos,verify=False)

#obtém página html
html = req.text
#objetivo beautifulsoup
soup = BeautifulSoup(html,"html.parser")

#procura os concursos do TRT
links_tribunais = soup.find_all("a",string=re.compile("tribun\w+",re.IGNORECASE))

#dataframe para receber links e tribunais
df_links = pd.DataFrame(columns=['tribunal','link'])

#criar lista com tribunais e links
ls_tribunais = list()
for trt in links_tribunais:
    ls_tribunais.append([trt.text,trt.get('href')])
df_links = df_links.append(pd.DataFrame(ls_tribunais,columns=df_links.columns),ignore_index=True)
print(df_links)