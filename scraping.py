from bs4 import BeautifulSoup
import requests

req = requests.get("https://example.com")


print(req.text)

soup = BeautifulSoup(req.text)

print(soup)
soup.select("title")
type(soup.select("title"))
type(soup.select("title")[0])
soup.select("title")[0].getText()
soup.select("h1")
soup.select("p")
# Seleccionar del segundo parágrafo el primer enlace
a = soup.select("p")[1].select("a")[0]

# Mostrar su contenido
a.getText()
# Atributo con la dirección del enlace
a['href']
a.attrs.items()
for meta in soup.select("meta"):
    for atributo, valor in meta.attrs.items():
        print(f"{atributo}: {valor}")
