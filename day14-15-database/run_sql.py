import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Read and execute the SQL file
with open('queries.sql', 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)

# Insert a test employee
cursor.execute("INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES ('1', 'Test User', 'HR', 50000)")
conn.commit()

print("--- DATABASE CREATED AND QUERIES EXECUTED ---")
print("\nEmployees List:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

conn.close()