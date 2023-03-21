import requests
from bs4 import BeautifulSoup

req = requests.get(
    "https://web.archive.org/web/20220722211457/https://es.wikipedia.org/wiki/Python")
soup = BeautifulSoup(req.text)

title = soup.select("title")[0].getText()
print(title)


resumen = soup.select("p")[0].getText()
print(resumen)


toc = soup.select("#toc")[0]

for a in toc.select("a"):
    print(a.getText())
