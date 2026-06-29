import sqlite3

def get_db_connection():
    # Connects to the file you just created
    conn = sqlite3.connect('company.db')
    # This makes the data output like a dictionary
    conn.row_factory = sqlite3.Row 
    return conn