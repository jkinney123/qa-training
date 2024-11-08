import database

# Create the database if it doesn't exist
database.create_database()

# database.create_user('Joe', 40)
# database.create_user('Tom', 30) 
# database.create_user('Bob', 20) 

database.update_user(1, 'New York')  # Update user with ID 1
database.update_user(2, 'Chicago')
database.update_user(3, 'San francisco')
database.update_user(4, 'Minneapolis')
# database.update_user(5, 'Seattle')

database.delete_user('Alice', 'San francisco')


database.print_database()
