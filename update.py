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
# Example of updating data in the table
update_data_query = """
UPDATE test_table SET age = %s WHERE name = %s
"""
new_age = 23
name_to_update = "John Doe"
cursor.execute(update_data_query, (new_age, name_to_update))
db_connection.commit()