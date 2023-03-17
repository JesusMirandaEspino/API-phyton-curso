import requests

dominio = "http://127.0.0.1:8000"
# dominio = "https://vlavj0.deta.dev"

r = requests.get(f"{dominio}/clientes")

print(r.text)


for cliente in r.json():
    print(cliente['dni'], cliente['nombre'], cliente['apellido'])
