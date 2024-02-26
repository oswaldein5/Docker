from tkinter import messagebox as MessageBox
import psycopg2
from psycopg2 import OperationalError

# Defining database connection parameters
db_params = {
    "host": "postg",
    "database": "postgres",
    "user": "postgres",
    "password": "prueba",
    "port": "5432"
}

try: 
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Set the client encoding to UTF-8
    #conn.set_client_encoding('UTF8')

    # Create a cursor object using the cursor() method
    cur = conn.cursor()

    # Execute a SQL query
    cur.execute("SELECT version()")

    # Fetch the results
    db_version = cur.fetchone()
    print("Si entro a la App Dockerizada...")
    print("PostgreSQL database version:", db_version)
    #MessageBox.showinfo("Probando Docker", db_version)

    # Close the cursor and connection
    cur.close()
    conn.close()
except OperationalError as e:
    print(f"Error: {e}")
    #MessageBox.showinfo("Probando Docker", f"Error: {e}")