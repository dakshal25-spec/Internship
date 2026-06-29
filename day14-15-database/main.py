from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import db

app = FastAPI()

class Employee(BaseModel):
    id: str
    name: str
    department: str
    salary: int

@app.get("/employees")
def get_all_employees():
    conn = db.get_db_connection()
    employees = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return [dict(emp) for emp in employees]

@app.post("/employees")
def add_employee(emp: Employee):
    conn = db.get_db_connection()
    try:
        conn.execute("INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)", 
                     (emp.id, emp.name, emp.department, emp.salary))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    conn.close()
    return {"message": "Employee added successfully"}