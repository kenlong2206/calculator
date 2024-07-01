# tests/unit/test_main.py

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.logging_setup import setup_logging

# Create a test client using FastAPI's TestClient
client = TestClient(app)

# Set up logging
logger = setup_logging()


def test_read_root():
    # Test the root endpoint '/'
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the calculator API!'}

def test_calculate_add():
    # Test the '/calculate' endpoint for addition
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "add"})
    assert response.status_code == 200
    assert response.json()["result"] == 15.0

def test_calculate_subtract():
    # Test the '/calculate' endpoint for subtraction
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "subtract"})
    assert response.status_code == 200
    assert response.json()["result"] == 5.0

def test_calculate_multiply():
    # Test the '/calculate' endpoint for multiplication
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "multiply"})
    assert response.status_code == 200
    assert response.json()["result"] == 50.0

def test_calculate_divide():
    # Test the '/calculate' endpoint for division
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "divide"})
    assert response.status_code == 200
    assert response.json()["result"] == 2.0

def test_calculate_divide_by_zero():
    # Test the '/calculate' endpoint for division by zero
    response = client.post("/calculate", json={"num1": 10, "num2": 0, "operation": "divide"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero is not allowed"

def test_calculate_invalid_operation():
    # Test the '/calculate' endpoint for an invalid operation
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "invalid"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid operation. Supported operations: add, subtract, multiply, divide"
