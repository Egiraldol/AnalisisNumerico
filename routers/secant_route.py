from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.secant_method import secant_method

# Definir un esquema de entrada con Pydantic
class SecantInput(BaseModel):
    xi: float
    xs: float
    tol: float
    niter: int
    function: str

# Crear el router para las rutas de este módulo
router = APIRouter()

# Endpoint que llama al método de la secante
@router.post("/secant/")
async def secant(input_data: SecantInput):
    try:
        result = secant_method(input_data.xi, input_data.xs, input_data.tol, input_data.niter, input_data.function)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
