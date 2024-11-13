import database

# Create the database if it doesn't exist
database.create_database()

# database.create_user('Joe', 40)
# database.create_user('Tom', 30) 
# database.create_user('Bob', 20) 

database.update_user(7, 'Los Angeles') 
database.update_user(6, 'Reseda')
# database.update_user(5, 'Seattle')




database.print_database()
