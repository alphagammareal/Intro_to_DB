import mysql.connector

try:
    # Try to connect to MySQL Server (no database yet)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="AlphaSql@2000"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Create database if it doesn't already exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    # Catch and display any connection or SQL error
    print("Error while connecting to MySQL:", err)

finally:
    # Ensure resources are cleaned up properly
    try:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed.")
    except NameError:
        # 'mydb' may not exist if connection failed
        print("Connection was not established, nothing to close.")
