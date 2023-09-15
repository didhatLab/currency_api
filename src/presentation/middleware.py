from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.application.exeption import CurrencyApiError


async def handle_service_error(_, exc: CurrencyApiError):
    return JSONResponse(
        status_code=400,
        content={"error": exc.error}
    )



def setup_middlewares(app: FastAPI):
    app.exception_handler(CurrencyApiError)(handle_service_error)
    
