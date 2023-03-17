from requests import HTTPError
import requests

dominio = "http://127.0.0.1:8000"
# dominio = "https://vlavj0.deta.dev"

r = requests.get(f"{dominio}/clientes")

print(r.text)
for cliente in r.json():
    print(cliente['dni'], cliente['nombre'], cliente['apellido'])


dni = "48H"
r = requests.get(f"{dominio}/clientes/buscar/{dni}")
print(r.text)
cliente = r.json()
print(cliente['dni'], cliente['nombre'], cliente['apellido'])


dominio = "http://127.0.0.1:8000"
dni = "99Z"

try:
    r = requests.get(f"{dominio}/clientes/buscar/{dni}")
    r.raise_for_status()
    r.json()
    print(cliente['dni'], cliente['nombre'], cliente['apellido'])
except HTTPError as ex:
    print(ex)


dominio = "http://127.0.0.1:8000"

payload = {
    'dni': '99Z',
    'nombre': 'Hector',
    'apellido': 'Costa'
}

r = requests.post(f"{dominio}/clientes/crear/", data=payload)
print(r.text)


r = requests.get(f"{dominio}/clientes")

for cliente in r.json():
    print(cliente['dni'], cliente['nombre'], cliente['apellido'])


dominio = "http://127.0.0.1:8000"
dni = '99Z'

r = requests.delete(f"{dominio}/clientes/borrar/{dni}")
print(r.text)


r = requests.get(f"{dominio}/clientes")

for cliente in r.json():
    print(cliente['dni'], cliente['nombre'], cliente['apellido'])


dni = '99Z'

r = requests.delete(f"{dominio}/clientes/borrar/{dni}")
print(r.text)


r.status_code
