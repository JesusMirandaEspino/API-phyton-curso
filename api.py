from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db
from pydantic import BaseModel, constr, validator
import helpers


class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente):
    @validator("dni")
    def validar_dni(cls, dni):
        if not helpers.dni_valido(dni, db.Clientes.lista):
            raise ValueError("Cliente ya existente o DNI incorrecto")
        return dni

app = FastAPI()

headers = {"content-type": "charset=utf-8"}

@app.get("/")
async def index():
    content = {'mensaje': '¡Hola mundo!'}
    return JSONResponse(content=content, headers=headers,  media_type="application/json")


@app.get("/html/")
def html():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content, media_type="text/html")


@app.get("/clientes/")
async def clientes():
    content = content = [
        cliente.to_dict() for cliente in db.Clientes.lista
    ]
    headers = {"content-type": "charset=utf-8"}
    return JSONResponse(content=content, headers=headers)


@app.get("/clientes/buscar/{dni}/")
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    headers = {"content-type": "charset=utf-8"}
    return JSONResponse(content=cliente.to_dict(), headers=headers)


@app.post("/clientes/crear/")
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        headers = {"content-type": "charset=utf-8"}
        return JSONResponse(content=content.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


print("Servidor de la API...")
