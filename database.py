import sqlite3


def create_database():
            # Create a connection to the database (it will be created if it doesn't exist)
            conn = sqlite3.connect('mydatabase.db')

            # Create a cursor object to execute SQL commands
            cursor = conn.cursor()

            # Create a table (if it doesn't exist)
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
                )''')
          #  cursor.execute("ALTER TABLE users ADD COLUMN city TEXT;") 

            # Commit the changes
            conn.commit()

            # Close the connection
            conn.close()

            print("SQLite database created successfully!")



def create_user(name, age):
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                      (name, age))

            conn.commit()
            conn.close()

def update_user(user_id, city):
    """Updates the city for a user in the database.
    Args:
        user_id (int): The ID of the user to update.
        city (str): The new city for the user.
    """
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("UPDATE users SET city = ? WHERE id = ?", (city, user_id))
    conn.commit()
    conn.close()


def delete_user(name, city):
    """Deletes a user from the database based on their name.
    Args:
        name (str): The name of the user to delete.
    """
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE name = ? AND city = ?", (name, city))
    conn.commit()
    conn.close()


def print_database():
            # Create a connection to the database
            conn = sqlite3.connect('mydatabase.db')
            # Create a cursor object to execute SQL commands
            cursor = conn.cursor()
            # Execute a SELECT query to retrieve all rows from the table
            cursor.execute("SELECT * FROM users")
            # Fetch all rows from the result set
            rows = cursor.fetchall()
            # Print the rows
            for row in rows:
                        print(row)
            # Close the connection
            conn.close()
