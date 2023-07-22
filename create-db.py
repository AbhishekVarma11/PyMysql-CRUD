
import mysql.connector

# Replace with your MySQL server details
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)


# Create a cursor to execute SQL queries
cursor = db_connection.cursor()

# Replace 'your_database_name' with your desired database name
create_database_query = "CREATE DATABASE test_db"
cursor.execute(create_database_query)

# Commit the changes
db_connection.commit()

# Close the cursor and the connection
cursor.close()
db_connection.close()
