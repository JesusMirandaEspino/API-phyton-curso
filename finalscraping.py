import os
import csv
import requests
from bs4 import BeautifulSoup


def scrap_quotes(url=""):
    domain = "https://quotes.toscrape.com"
    req = requests.get(f"{domain}{url}")
    soup = BeautifulSoup(req.text)

    quotes = []
    quotes_tags = soup.select("div.quote")
    for quote_tag in quotes_tags:
        quote = {}
        quote['text'] = quote_tag.select("span.text")[0].getText()
        quote['author'] = quote_tag.select("small.author")[0].getText()
        quote['tags'] = []
        for tag in quote_tag.select("div.tags a.tag"):
            quote['tags'].append(tag.getText())
        quotes.append(quote)

    next_url = None
    link_tag = soup.select("li.next a")
    if len(link_tag) > 0:
        next_url = link_tag[0]['href']

    print(f"Página {domain}{url}, {len(quotes)} citas scrapeadas.")

    return quotes, next_url


def scrap_site(limit=2):
    all_quotes = []
    next_url = ""
    while 1:
        quotes, next_url = scrap_quotes(next_url)
        all_quotes += quotes
        limit -= 1
        if limit == 0 or next_url == None:
            return all_quotes


class Citas:
    quotes = []

    if os.path.exists("quotes.csv"):
        with open("quotes.csv", "r") as file:
            data = csv.DictReader(file)
            for quote in data:
                quote['tags'] = eval(quote['tags'])
                quotes.append(quote)

    @staticmethod
    def scrapear():
        Citas.quotes = scrap_site(limit=99)  # <--- LIMITE MUY GRANDE
        with open("quotes.csv", "w") as file:
            writer = csv.DictWriter(
                file, fieldnames=["text", "author", "tags"])
            writer.writeheader()
            for quote in Citas.quotes:
                writer.writerow(quote)

    @staticmethod
    def listar(limite=10):
        for quote in Citas.quotes[:limite]:
            print(quote["text"])
            print(quote["author"])
            for tag in quote["tags"]:
                print(tag, end=" ")
            print("\n")

    @staticmethod
    def etiqueta(nombre=""):
        for quote in Citas.quotes:
            if nombre in quote["tags"]:
                print(quote["text"])
                print(quote["author"])
                for tag in quote["tags"]:
                    print(tag, end=" ")
                print("\n")

    @staticmethod
    def autor(nombre=""):
        for quote in Citas.quotes:
            if nombre == quote["author"]:
                print(quote["text"])
                print(quote["author"])
                for tag in quote["tags"]:
                    print(tag, end=" ")
                print("\n")
