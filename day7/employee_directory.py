import json

FILE_NAME = "employees.json"


def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


def add_employee():

    employees = load_employees()

    emp_id = input("Enter ID: ")

    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee ID already exists.")
            return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employees.append(
        {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        }
    )

    save_employees(employees)

    print("Employee added successfully.")


def view_employees():

    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    print("\n----- Employee List -----")

    for employee in employees:

        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Salary: {employee['salary']}")

        print("--------------------")


def search_employee():

    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for employee in employees:

        if employee["id"] == emp_id:

            print("\nEmployee Found")

            print(f"ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Salary: {employee['salary']}")

            return

    print("Employee not found.")


def update_employee():

    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for employee in employees:

        if employee["id"] == emp_id:

            employee["name"] = input("Enter New Name: ")

            employee["department"] = input(
                "Enter New Department: "
            )

            employee["salary"] = float(
                input("Enter New Salary: ")
            )

            save_employees(employees)

            print("Employee updated successfully.")

            return

    print("Employee not found.")


def delete_employee():

    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for employee in employees:

        if employee["id"] == emp_id:

            employees.remove(employee)

            save_employees(employees)

            print("Employee deleted successfully.")

            return

    print("Employee not found.")


def main():

    while True:

        print("\n---- Employee Directory ----")

        print("1. Add Employee")

        print("2. View All Employees")

        print("3. Search Employee")

        print("4. Update Employee")

        print("5. Delete Employee")

        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_employee()

        elif choice == "2":

            view_employees()

        elif choice == "3":

            search_employee()

        elif choice == "4":

            update_employee()

        elif choice == "5":

            delete_employee()

        elif choice == "6":

            print("Exiting...")

            break

        else:

            print("Invalid choice.")


main()