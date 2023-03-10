from fastapi import FastAPI
from fastapi.responses import JSONResponse


@app.get("/")
async def index():
    content = {'mensaje': '¡Hola mundo!'}
    return JSONResponse(content=content)

print("Servidor de la API...")
