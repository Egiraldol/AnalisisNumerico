from fastapi import FastAPI
from routers.secant_route import router as secant_router

app = FastAPI()

# Incluir las rutas del método secante
app.include_router(secant_router)

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de métodos numéricos"}
