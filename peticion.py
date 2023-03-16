from requests.exceptions import Timeout
from requests import HTTPError
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

url = 'https://httpbin.org/post'

payload = {
    'nombre': 'Hector Costa Guzman',
    'intereses': ['Python', 'Videojuegos'],
    'edad': 33,
}

r = requests.post(url, json=payload)

print(r.text)


r = requests.get('https://httpbin.org/status/404')
print(r.status_code)


try:
    # Hacemos la petición al sitio de pruebas
    r = requests.get("https://httpbin.org/status/404")
    # Pedimos que se invoque una excepcion HTTPError si hay algún fallo
    r.raise_for_status()
    # Si no hay un fallo mostramos algo de prueba
    print(r.status_code)
except HTTPError as ex:
    # Si se ha invocado una excepción HTTPError mostramos el resultado
    print(ex)


r = requests.get('https://httpbin.org/delay/5')


print(r.status_code)


r = requests.get('https://httpbin.org/delay/5', timeout=3)


try:
    requests.get('https://httpbin.org/delay/5', timeout=3)
except Timeout:
    print("ERROR: La petición ha tardado más de 3 segundos")
