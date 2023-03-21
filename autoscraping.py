import csv
import requests
from bs4 import BeautifulSoup

req = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(req.text)

# Buscamos las citas de la portada
quotes_tags = soup.select("div.quote")
for quote_tag in quotes_tags:
    # Buscamos el texto
    print(quote_tag.select("span.text")[0].getText())
    # Buscamos el autor
    print(quote_tag.select("small.author")[0].getText())
    # Buscamos las etiquetas
    for tag in quote_tag.select("div.tags a.tag"):
        print(tag.getText(), end=" ")
    # Salto de línea para separar las citas
    print("\n")


def scrap_quotes(url=""):
    domain = "https://quotes.toscrape.com"
    req = requests.get(f"{domain}{url}")
    soup = BeautifulSoup(req.text)

    # Lista para almacenar diccionarios que contendrán datos de las citas
    quotes = []
    # Buscamos las citas de la portada
    quotes_tags = soup.select("div.quote")
    for quote_tag in quotes_tags:
        # Creamos un diccionario vacío
        quote = {}
        # Almacenamos los diferentes campos en el diccinario
        quote['text'] = quote_tag.select("span.text")[0].getText()
        quote['author'] = quote_tag.select("small.author")[0].getText()
        quote['tags'] = []
        for tag in quote_tag.select("div.tags a.tag"):
            quote['tags'].append(tag.getText())
        # Añadimos el diccionario con la cita a la lista
        quotes.append(quote)
    # Devolvemos las citas scrapeadas
    return quotes


quotes = scrap_quotes()

for quote in quotes:
    print(quote["text"])
    print(quote["author"])
    for tag in quote["tags"]:
        print(tag, end=" ")
    print("\n")


domain = "https://quotes.toscrape.com"
req = requests.get(domain)
soup = BeautifulSoup(req.text)

# Buscamos el enlace en el tag li con clase next
link_tag = soup.select("li.next a")
# Si hay como mínimo un enlace extraemos su href relativo sumado al dominio
if len(link_tag) > 0:
    next_url = link_tag[0]['href']
    print(next_url)


def scrap_quotes(url=""):
    domain = "https://quotes.toscrape.com"
    req = requests.get(f"{domain}{url}")
    soup = BeautifulSoup(req.text)

    # Lista para almacenar diccionarios que contendrán datos de las citas
    quotes = []
    # Buscamos las citas de la portada
    quotes_tags = soup.select("div.quote")
    for quote_tag in quotes_tags:
        # Creamos un diccionario vacío
        quote = {}
        # Almacenamos los diferentes campos en el diccinario
        quote['text'] = quote_tag.select("span.text")[0].getText()
        quote['author'] = quote_tag.select("small.author")[0].getText()
        quote['tags'] = []
        for tag in quote_tag.select("div.tags a.tag"):
            quote['tags'].append(tag.getText())
        # Añadimos el diccionario con la cita a la lista
        quotes.append(quote)

    # Buscamos el enlace en el tag li con clase next
    next_url = None
    link_tag = soup.select("li.next a")
    # Si hay como mínimo un enlace extraemos su href relativo sumado al dominio
    if len(link_tag) > 0:
        next_url = link_tag[0]['href']

    # Imprimiros un mensaje informativo
    print(f"Página {domain}{url}, {len(quotes)} citas scrapeadas.")

    # Devolvemos las citas scrapeadas y la siguiente página, que puede ser None
    return quotes, next_url


quotes, next_url = scrap_quotes()

print()  # Espacio en blanco
print(next_url)


def scrap_site(limit=2):
    # Definimos una lista global para almacenar todas las citas
    all_quotes = []
    # Definimos la siguiente URL que irá cambiando (inicialmente es el dominio raíz)
    next_url = ""
    # Iniciamos un bucle infinito
    while 1:
        # Scrapeamos la página, guardamos las citas scrapeadas y la siguiente página
        quotes, next_url = scrap_quotes(next_url)
        # Añadimos las citas scrapeadas a la lista global
        all_quotes += quotes
        # Restamos 1 al limite
        limit -= 1
        # Si lo superamos o no hay siguiente página finalizamos la función
        if limit == 0 or next_url == None:
            # Finalizamos la función
            return all_quotes


quotes = scrap_site()

print()  # Espacio en blanco
for quote in quotes:
    print(quote["text"])
    print(quote["author"])
    for tag in quote["tags"]:
        print(tag, end=" ")
    print("\n")


class Citas:

    # Variable de clase para almacenar las citas en la memoria
    quotes = []

    @staticmethod
    def scrapear():
        # Scrapeamos todas las citas, ponemos un límite pequeño para hacer pruebas
        Citas.quotes = scrap_site(limit=2)
        # Guardamos las citas scrapeadas en un fichero CSV volcándolas de la lista de dicts
        with open("quotes.csv", "w") as file:
            # Definimos el objeto para escribir con las cabeceras de los campos
            writer = csv.DictWriter(
                file, fieldnames=["text", "author", "tags"])
            # Escribimos las cabeceras
            writer.writeheader()
            # Escribimos cada cita en la memoria en el fichero
            for quote in Citas.quotes:
                writer.writerow(quote)


Citas.scrapear()
