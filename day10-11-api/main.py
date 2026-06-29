from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory list to store employees
employees_db = [
    {"id": "101", "name": "John", "department": "HR", "salary": 50000.0}
]

# Required format for adding an employee
class Employee(BaseModel):
    id: str
    name: str
    department: str
    salary: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/employees")
def get_employees():
    return employees_db

@app.post("/employees")
def add_employee(emp: Employee):
    employees_db.append(emp.dict())
    return {"message": "Employee added successfully"}