class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = float(salary)

class EmployeeManager:
    def __init__(self):
        # Using a dictionary to easily store and find employees by their ID
        self.employees = {}

    def add_employee(self):
        emp_id = input("\nEnter ID: ")
        if emp_id in self.employees:
            print("Error: Employee ID already exists.")
            return
        
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")
        
        # Create a new Employee object and store it
        new_employee = Employee(emp_id, name, department, salary)
        self.employees[emp_id] = new_employee
        print("\nEmployee added successfully.")

    def view_employees(self):
        if not self.employees:
            print("\nNo employees found. Please add an employee first.")
            return
            
        print("\n--- All Employees ---")
        for emp_id, emp in self.employees.items():
            print(f"ID: {emp.emp_id} | Name: {emp.name} | Dept: {emp.department} | Salary: {emp.salary}")

    def search_employee(self):
        emp_id = input("\nEnter ID to search: ")
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print("\n--- Employee Found ---")
            print(f"ID: {emp.emp_id}")
            print(f"Name: {emp.name}")
            print(f"Department: {emp.department}")
            print(f"Salary: {emp.salary}")
        else:
            print("\nError: Employee not found.")

    def update_employee(self):
        emp_id = input("\nEnter ID to update: ")
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print("\nLeave the field blank and press Enter if you do not want to change it.")
            
            new_name = input(f"Enter new Name [{emp.name}]: ")
            if new_name: 
                emp.name = new_name
                
            new_dept = input(f"Enter new Department [{emp.department}]: ")
            if new_dept: 
                emp.department = new_dept
                
            new_salary = input(f"Enter new Salary [{emp.salary}]: ")
            if new_salary: 
                emp.salary = float(new_salary)
                
            print("\nEmployee updated successfully.")
        else:
            print("\nError: Employee not found.")

    def delete_employee(self):
        emp_id = input("\nEnter ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("\nEmployee deleted successfully.")
        else:
            print("\nError: Employee not found.")

def main():
    manager = EmployeeManager()
    
    while True:
        print("\n---- Employee Management System ----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            manager.search_employee()
        elif choice == '4':
            manager.update_employee()
        elif choice == '5':
            manager.delete_employee()
        elif choice == '6':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

# This ensures the menu runs when the script is started
if __name__ == "__main__":
    main()