import pyodbc
from util import db_property_util

def get_db_connection():
    connection_string = db_property_util.DBPropertyUtil.get_connection_string()
    return pyodbc.connect(connection_string)

def register_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    query = """
    INSERT INTO [User] (Username, Password, Email, FirstName, LastName)
    VALUES (?, ?, ?, ?, ?)
    """
    values = (username, password, email, first_name, last_name)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("✅ Registration successful!")

def login_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")

    query = """
    SELECT UserID, FirstName FROM [User] WHERE Username = ? AND Password = ?
    """
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"✅ Login successful. Welcome, {user.FirstName}!")
        return user.UserID
    else:
        print("❌ Invalid username or password.")
        return None
