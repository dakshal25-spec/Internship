from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic Models
class Employee(BaseModel):
    id: str
    name: str
    department: str
    salary: float

class EmployeeUpdate(BaseModel):
    name: str
    department: str
    salary: float

# In-Memory Database
db = {}

# 1. Add Employee (POST)
@app.post("/employees")
def add_employee(emp: Employee):
    if emp.id in db:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    db[emp.id] = emp
    return {"message": "Employee added successfully"}

# 2. Get All Employees (GET)
@app.get("/employees")
def get_all_employees():
    return db

# 3. Get Employee by ID (GET)
@app.get("/employees/{id}")
def get_employee(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db[id]

# 4. Update Employee (PUT)
@app.put("/employees/{id}")
def update_employee(id: str, emp_update: EmployeeUpdate):
    if id not in db:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Update the values
    db[id].name = emp_update.name
    db[id].department = emp_update.department
    db[id].salary = emp_update.salary
    return {"message": "Employee updated successfully"}

# 5. Delete Employee (DELETE)
@app.delete("/employees/{id}")
def delete_employee(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Employee not found")
    del db[id]
    return {"message": "Employee deleted successfully"}