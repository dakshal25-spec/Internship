def get_employees():
    return {
        "101": {"Name": "Alice", "Department": "HR", "Salary": 50000},
        "102": {"Name": "Bob", "Department": "Engineering", "Salary": 80000},
        "103": {"Name": "Charlie", "Department": "Marketing", "Salary": 60000}
    }

def search_employee(employees, search_id):
    if search_id in employees:
        details = employees[search_id]
        print("\n--- Employee Found ---")
        print(f"Name: {details['Name']}")
        print(f"Department: {details['Department']}")
        print(f"Salary: {details['Salary']}")
    else:
        print(f"\nError: Employee ID '{search_id}' does not exist.")

def main():
    employees = get_employees()
    emp_id_to_search = input("Enter Employee ID to search (e.g., 101, 102): ")
    search_employee(employees, emp_id_to_search)

main()