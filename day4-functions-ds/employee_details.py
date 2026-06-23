def get_employees():
    employees = {
        "101": {"Name": "Alice", "Department": "HR", "Salary": 50000},
        "102": {"Name": "Bob", "Department": "Engineering", "Salary": 80000},
        "103": {"Name": "Charlie", "Department": "Marketing", "Salary": 60000}
    }
    return employees

def display_employees(employees):
    print("--- Employee Details ---")
    for emp_id, details in employees.items():
        print(f"ID: {emp_id} | Name: {details['Name']} | Dept: {details['Department']} | Salary: {details['Salary']}")

def main():
    employees = get_employees()
    display_employees(employees)

main()