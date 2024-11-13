from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.multiple_roots_method import multiple_roots_method

# Define the input schema with Pydantic
class MultipleRootsInput(BaseModel):
    x0: float
    tol: float
    niter: int
    function: str
    derivative1: str
    derivative2: str

# Create the router for this module
router = APIRouter()

# Endpoint that calls the Multiple Roots method
@router.post("/multiple_roots/")
async def multiple_roots(input_data: MultipleRootsInput):
    try:
        result = multiple_roots_method(
            input_data.x0,
            input_data.tol,
            input_data.niter,
            input_data.function,
            input_data.derivative1,
            input_data.derivative2
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
