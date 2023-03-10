from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

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

print("Servidor de la API...")
