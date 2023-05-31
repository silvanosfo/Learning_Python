import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.cmjornal.pt/cm-ao-minuto')

#print(response.content)
#print(type(response.content))

content = response.content

site = BeautifulSoup(content, 'html.parser')

#print(type(site))

#print(site.prettify())

#obter o html da noticia
noticia = site.find('div', attrs={'class': 'aominutoMain'})
#print(noticia)
#print(noticia.prettify())

#obter o titulo da noticia
titulo = noticia.find('span', attrs={'class': 'lead'})
#print(titulo)
print(titulo.text)
#print(titulo['href'])

dataN = noticia.find('a', attrs={'data-action': 'DestaquesPrincipais'})
print(dataN.text)
#noticiatitulo = noticia.find('h2', attrs={'class': 't-stamp-4'})
#print(noticiatitulo.text)
#Para obter somente o texto da noticia
#print(titulo.text)