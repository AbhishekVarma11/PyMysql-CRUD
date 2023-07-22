import mysql.connector

# Replace with your MySQL database credentials
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
# Example of deleting data from the table
delete_data_query = """
DELETE FROM test_table WHERE name = %s
"""
name_to_delete = "John Doe"
cursor.execute(delete_data_query, (name_to_delete,))
db_connection.commit()