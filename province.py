#esercizio consegna
import urllib.request
address ='https://www.comuni-italiani.it/province.html'
response = urllib.request.urlopen(address)
theBytes = response.read()
html = theBytes.decode("latin-1") #che sarebbe lettura in encoding , "iso - 8859-1"
print(len(html))

from bs4 import BeautifulSoup
doc = BeautifulSoup(html, "html.parser")
#print(doc.prettify()) #fatto per analizzare il codice nella sua interezza

t1= doc.table
t2 = t1.find_next("table") #viaggio di riga in riga TR per ogni tabella fino a quella che mi serve
t3 = t2.find_next("table")
t4= t3.find_next("table")
riga = t4.find_next("tr")

#esercizio trasformando in pandas
import pandas as pd
province = pd.DataFrame(columns = ["sigla", "nome" , "abitanti"])
i =0 #per ciclare

riga = riga.find_next("tr") #per trovare la riga di agrigemto AG
print(riga)

#t1 = BeautifulSoup(html, "html.parser").table
#t2 = t1.find_next("table")
#t3 = t2.find_next("table")
#t4 = t3.find_next("table")
#riga = t4.find_next("tr")
#riga = riga.find_next("tr")

#province = {} #voglio creare un dictionary con coppie chiave-valore , nel secondo esempio lo trasformo ion database e non mi serve piu
while riga != None :
  tdx = riga.find_next("td") #td sta per *table data* usato per css
  tdx = tdx.find_next("td")
  provincia = tdx.get_text() #why
  #print (tdx.get_text())
  tdx = tdx.find_next("td")
  residenti = tdx.get_text() #sono 6 colonne saltate per arrivare al dato che voleva
  residenti = residenti.replace(".", "").strip()
  residenti = int(residenti)  # Converte la stringa in intero
  tdx = tdx.find_next("td")
  tdx = tdx.find_next("td")
  tdx = tdx.find_next("td")
  tdx = tdx.find_next("td")
  tdx = tdx.find_next("td")
  sigla = tdx.get_text()
  province.loc[i] = [sigla, provincia, residenti]
  if sigla == 'VT' : break
  i += 1  #aggiunta per conteggio
  riga = riga.find_next("tr")

#print(province)

#l= dir(province )
#print(l)

print(province.sort_values (by= "abitanti", ascending = False ) ) #( by ascending=False)

import pickle

with open('status.pkl', 'wb') as dbfile:
    pickle.dump(province, dbfile)  # Salvataggio del DataFrame in pickle
