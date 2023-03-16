import requests

r = requests.get('https://www.wikipedia.es/')

print(type(r)) # tipo del dato

print(r.headers['date'])             # fecha de la petición
print(r.headers['last-modified'])    # fecha de última modificación
print(r.headers['content-type'])     # tipo del contenido
print(r.headers['server'])           # servidor
print(r.headers['content-language'])  # idioma


url = 'https://httpbin.org/get'

payload = {
    'nombre': 'Hector Costa Guzman',
    'intereses': ['Python', 'Videojuegos'],
    'edad': 33,
}

r = requests.get(url, params=payload)

print(r.text)


url = 'https://httpbin.org/post'

payload = {
    'nombre': 'Hector Costa Guzman',
    'intereses': ['Python', 'Videojuegos'],
    'edad': 33,
}

r = requests.post(url, data=payload)

print(r.text)
