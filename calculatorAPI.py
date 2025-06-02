from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operation(BaseModel):
    num1: float
    num2: float
    process: str  # "add" or "sub"
def success_response(key: str, value: float):
    return {
        "Status": [{"MessageCode": "S", "MessageText": "OK"}],
        "ReturnData": [{key: value}]
    }

# Validation
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "Status": [{"MessageCode": "E", "MessageText": "Error"}],
            "ReturnData": [{"Invalid input format. num1 and num2 must be numbers."}]
        },
    )

@app.post("/calculate")
def calculate(op: Operation):
    if op.process == "add":
        result = op.num1 + op.num2
        return success_response("addition", result)
    elif op.process == "sub":
        result = op.num1 - op.num2
        return success_response("subtraction", result)
    else:
        return {
            "Status": [{"MessageCode": "E", "MessageText": "Invalid process type. Use 'add' or 'sub'."}],
            "ReturnData": []
        }
