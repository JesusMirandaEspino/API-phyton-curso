import requests
from bs4 import BeautifulSoup
import re

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



for a in toc.select("a"):
    text = a.getText()
    if re.match(r"\d+ ", text):
        print(text)


for a in toc.select("a"):
    text = a.getText()
    if re.match(r"\d+ ", text):
        print(text)
    elif re.match(r"\d+.\d+ ", text):
        print(" ", text)
    elif re.match(r"\d+.\d+.\d+ ", text):
        print("   ", text)


tr_tags = soup.select(".infobox tr")

for tr_tag in tr_tags:
    print(tr_tag.getText())


tr_tags = soup.select(".infobox tr")

for tr_tag in tr_tags:
    th_tags = tr_tag.select("th")
    td_tags = tr_tag.select("td")
    if len(th_tags) > 0 and len(td_tags) > 0:
        print(
            f"{th_tags[0].getText().strip()}: {td_tags[0].getText().strip()}")
