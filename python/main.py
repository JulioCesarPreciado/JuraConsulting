from urllib.request import urlopen
import bs4
import pandas as pd
import numpy as np

url = 'http://ligamx.net/'
html = urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")

sections = soup.findAll("section")

#print(sections[0].findAll("li"))

#default tbl_grals

"""
for section in sections[0].findAll("li"):
    for equipo in section.findAll("img"):
        print(equipo.get("alt"))
    for title in section.findAll("a"):
        print(title.get("title"))
"""
nombres = []
goles = []

for section in sections:
    for table in section.findAll('table',{'class':'default tbl_goleos'}):
        for nombre in table.findAll('a',{'class':'loadershow'}):
            if(nombre.get("title") != None):
                nombres.append(nombre.get("title"))
        for gol in table.findAll('a',{'class':'loadershow ganados'}):
            goles.append(gol.string)

i = 0
data = pd.DataFrame(columns=('Nombre','Goles'))

while(i<5):
    #print(nombres[i] + ' Goles: ' + goles[i])]
    data.loc[len(data)] = [nombres[i],goles[i]]
    i = i + 1

data.to_csv('goleo.csv')
data.to_excel('goleo.xlsx', sheet_name='Tabla')
data.to_json('goleo.json')
