from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.fixedpoint_method import fixedpoint_method

# Define the input schema with Pydantic
class FixedPointInput(BaseModel):
    x0: float
    tol: float
    niter: int
    function: str
    gfunction: str
# Create the router for this module
router = APIRouter()

# Endpoint that calls the Fixed Point method
@router.post("/fixed_point/")
async def fixed_point(input_data: FixedPointInput):
    try:
        result = fixedpoint_method(
            input_data.x0,
            input_data.tol,
            input_data.niter,
            input_data.function,
            input_data.gfunction
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
