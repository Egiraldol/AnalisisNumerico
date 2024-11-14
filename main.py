from fastapi import FastAPI
from routers import secant_route, newton_route, bisection_route, fixedpoint_route, multiple_roots_route, false_position_route

app = FastAPI()

# Incluir las rutas del método secante
app.include_router(secant_route.router)
app.include_router(newton_route.router)
app.include_router(bisection_route.router)
app.include_router(fixedpoint_route.router)
app.include_router(multiple_roots_route.router)
app.include_router(false_position_route.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de métodos numéricos"}
