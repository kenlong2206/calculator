# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()


# Define request body model
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str


# Define routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the calculator API!"}


@app.post("/calculate")
def calculate(request: CalculationRequest):
    num1 = request.num1
    num2 = request.num2
    operation = request.operation.lower()

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Supported operations: add, subtract, multiply, divide")

    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
