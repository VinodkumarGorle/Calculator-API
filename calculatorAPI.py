from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class Operation(BaseModel):
    num1: float
    num2: float
    process: str  # "add" or "sub"

# Response structure helper
def success_response(key: str, value: float):
    return {
        "Status": [
            {"MessageCode": "S", "MessageText": "OK"}
        ],
        "ReturnData": [
            {key: value}
        ]
    }

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
            "Status": [
                {"MessageCode": "E", "MessageText": "Invalid process type. Use 'add' or 'sub'."}
            ],
            "ReturnData": []
        }
