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
# Example of inserting data into the table
insert_data_query = """
INSERT INTO test_table (name, age) VALUES (%s, %s)
"""
data_to_insert = ("John Doe", 30)
cursor.execute(insert_data_query, data_to_insert)
db_connection.commit()