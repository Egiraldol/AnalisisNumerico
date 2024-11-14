from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.false_position_method import false_position_method

# Define input schema using Pydantic
class FalsePositionInput(BaseModel):
    xi: float
    xs: float
    tol: float
    niter: int
    function: str

# Create the router for this module
router = APIRouter()

# Endpoint for False Position method
@router.post("/false_position/")
async def false_position(input_data: FalsePositionInput):
    try:
        result = false_position_method(
            input_data.xi,
            input_data.xs,
            input_data.tol,
            input_data.niter,
            input_data.function
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
