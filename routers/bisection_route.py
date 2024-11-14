from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.bisection_method import bisection_method

# Define the input schema with Pydantic
class BisectionInput(BaseModel):
    a: float
    b: float
    tol: float
    niter: int
    function: str

# Create the router for this module
router = APIRouter()

# Endpoint that calls the Bisection method
@router.post("/bisection/")
async def bisection(input_data: BisectionInput):
    try:
        result = bisection_method(
            input_data.a,
            input_data.b,
            input_data.tol,
            input_data.niter,
            input_data.function
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
