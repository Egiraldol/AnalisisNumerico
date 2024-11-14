from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.newton_method import newton_method

# Define the input schema with Pydantic
class NewtonInput(BaseModel):
    x0: float
    tol: float
    niter: int
    function: str
    function_prime: str

# Create the router for this module
router = APIRouter()

# Endpoint that calls the Newton-Raphson method
@router.post("/newton/")
async def newton(input_data: NewtonInput):
    try:
        result = newton_method(
            input_data.x0,
            input_data.tol,
            input_data.niter,
            input_data.function,
            input_data.function_prime
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
