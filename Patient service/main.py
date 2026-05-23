from fastapi import FastAPI
import os

app = FastAPI(title="Patient Service")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Patient Service!"}

@app.get("/patients")
def get_patients():
    # This is dummy data for your hackathon
    return [
        {"id": 1, "name": "John Doe", "condition": "Healthy"},
        {"id": 2, "name": "Jane Smith", "condition": "Recovering"}
    ]