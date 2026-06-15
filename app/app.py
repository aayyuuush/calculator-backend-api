# handles API routes

import logging

from fastapi import FastAPI, HTTPException
from app.main import calculate
from app.models.request_model import CalculatorRequest


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("app/logs/calculator.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# FastAPI App Initialization
app = FastAPI(
    title="Calculator Backend API",
    description="Production-style calculator backend using FastAPI",
    version="1.0.0"
)


# Root Endpoint
@app.get("/")
def home():

    logger.info("Home endpoint called")

    return {
        "message": "Calculator Backend API is running"
    }


# Calculator Endpoint
@app.post("/calculate")
def calculator(request: CalculatorRequest):

    logger.info(
        f"Calculation API called with data: {request}"
    )

    try:

        result = calculate(
            x=request.x,
            y=request.y,
            operator=request.operator
        )

        logger.info(
            f"Calculation successful | Result: {result}"
        )

        return {
            "success": True,
            "result": result
        }

    except ValueError as error:

        logger.error(
            f"ValueError occurred: {str(error)}"
        )

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:

        logger.exception(
            f"Unexpected server error: {str(error)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )