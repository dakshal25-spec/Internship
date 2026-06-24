import csv
import os

FILE_NAME = 'employees.csv'

def process_csv_data(file_path):
    try:
        # Open the file in read mode
        with open(file_path, mode='r', newline='') as file:
            # DictReader automatically uses the first row (headers) as dictionary keys
            reader = csv.DictReader(file)
            employees = list(reader)
            
            if not employees:
                print("The CSV file is empty.")
                return None
                
            total_employees = len(employees)
            total_salary = 0
            highest_salary = float('-inf')
            lowest_salary = float('inf')
            dept_counts = {}
            
            for row in employees:
                salary = float(row['salary'])
                dept = row['department']
                
                # Math calculations
                total_salary += salary
                if salary > highest_salary:
                    highest_salary = salary
                if salary < lowest_salary:
                    lowest_salary = salary
                    
                # Department counter
                if dept in dept_counts:
                    dept_counts[dept] += 1
                else:
                    dept_counts[dept] = 1
                    
            average_salary = total_salary / total_employees
            
            # Return all the calculated data as a dictionary
            return {
                'total': total_employees,
                'average': average_salary,
                'highest': highest_salary,
                'lowest': lowest_salary,
                'departments': dept_counts
            }
            
    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
        return None

def print_report(report_data):
    if not report_data:
        return
        
    print("\n===== Employee Report =====")
    print(f"Total Employees     : {report_data['total']}")
    # The :.2f ensures the numbers print with exactly two decimal places
    print(f"Average Salary      : {report_data['average']:.2f}")
    print(f"Highest Salary      : {report_data['highest']:.2f}")
    print(f"Lowest Salary       : {report_data['lowest']:.2f}\n")
    
    print("Department-wise Count:")
    for dept, count in report_data['departments'].items():
        # The :<18 aligns the colons neatly by padding with spaces
        print(f"  {dept:<18}: {count}")
    print()

def main():
    report_data = process_csv_data(FILE_NAME)
    print_report(report_data)

if __name__ == "__main__":
    main()