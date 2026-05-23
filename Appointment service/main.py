from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Appointment Service")

appointments = []

doctors = [
    {"id": 1234, "name": "Sawoud", "specialization": "Cardiologist", "schedule": "9am-6pm", "week_off": "None", "status": "available"},
    {"id": 4321, "name": "Masoud", "specialization": "Neurology", "schedule": "9am-6pm", "week_off": "Tuesday", "status": "available"},
    {"id": 5678, "name": "Dawoud", "specialization": "ENT", "schedule": "9am-6pm", "week_off": "Wednesday", "status": "available"},
    {"id": 8765, "name": "Sheeba", "specialization": "Orthopedic", "schedule": "24x7", "week_off": "Thursday", "status": "emergency"},
    {"id": 7688, "name": "Kubra", "specialization": "General Physician", "schedule": "24x7", "week_off": "Friday", "status": "emergency"},
    {"id": 7726, "name": "Fatima", "specialization": "Dentist", "schedule": "9am-6pm", "week_off": "Saturday", "status": "available"}
]

class AppointmentBooking(BaseModel):
    patient_name: str
    doctor_id: int
    time_slot: str

@app.get("/")
def home():
    return {"status": "Appointment Service is active and running"}

@app.get("/doctors")
def get_doctors():
    return {"doctors": doctors}

@app.post("/book")
def book_appointment(booking: AppointmentBooking):
    appointments.append(booking.dict())
    return {"message": "Appointment booked successfully!", "details": booking}