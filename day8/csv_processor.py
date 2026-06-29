import csv
import os
import logging

# Set up the logging configuration to write to app.log
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

FILE_NAME = 'employees.csv'

def process_csv_data(file_path):
    logging.info("Application started")
    
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Catch scenario: Empty CSV file
            if not reader.fieldnames:
                print("Notice: The CSV file is completely empty.")
                logging.warning("Empty CSV file")
                logging.info("Application exited")
                return None
                
            total_employees = 0
            total_salary = 0
            highest_salary = float('-inf')
            lowest_salary = float('inf')
            dept_counts = {}
            
            # Start row count at 1 to account for the header row
            row_number = 1 
            
            for row in reader:
                row_number += 1
                try:
                    # Catch scenario: Missing column (KeyError)
                    dept = row['department']
                    salary_str = row['salary']
                    
                    # Catch scenario: Invalid data type like "abc" (ValueError)
                    salary = float(salary_str)
                    
                    # If everything is valid, do the math calculations
                    total_salary += salary
                    if salary > highest_salary: 
                        highest_salary = salary
                    if salary < lowest_salary: 
                        lowest_salary = salary
                        
                    if dept in dept_counts:
                        dept_counts[dept] += 1
                    else:
                        dept_counts[dept] = 1
                        
                    total_employees += 1
                    
                except KeyError as e:
                    print(f"Error: Missing column {e} in CSV.")
                    logging.error(f"Missing column {e} in CSV")
                    logging.info("Application exited")
                    return None
                    
                except ValueError:
                    logging.warning(f"Invalid salary '{salary_str}' on row {row_number}, skipping")
                    continue
            
            # Final check in case all rows were skipped
            if total_employees == 0:
                print("No valid employee records found to generate a report.")
                logging.info("Application exited")
                return None
                
            average_salary = total_salary / total_employees
            logging.info(f"Loaded {total_employees} employees from {file_path}")
            
            return {
                'total': total_employees,
                'average': average_salary,
                'highest': highest_salary,
                'lowest': lowest_salary,
                'departments': dept_counts
            }
            
    # Catch scenario: CSV file not found
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        logging.error(f"File not found: {file_path}")
        logging.info("Application exited")
        return None

def print_report(report_data):
    if not report_data:
        return
        
    print("\n===== Employee Report =====")
    print(f"Total Employees     : {report_data['total']}")
    print(f"Average Salary      : {report_data['average']:.2f}")
    print(f"Highest Salary      : {report_data['highest']:.2f}")
    print(f"Lowest Salary       : {report_data['lowest']:.2f}\n")
    
    print("Department-wise Count:")
    for dept, count in report_data['departments'].items():
        print(f"  {dept:<18}: {count}")
    print()
    logging.info("Report generated successfully")

def main():
    report_data = process_csv_data(FILE_NAME)
    if report_data:
        print_report(report_data)
        logging.info("Application exited")

if __name__ == "__main__":
    main()