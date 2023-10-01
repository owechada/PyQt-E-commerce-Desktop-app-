import sqlite3
from user import User

class UserManager:


    


    def __init__(self):
        self.db_file = "mydatabase.db"
        self.conn = None

        try:
            self.conn = sqlite3.connect(self.db_file)
            self.create_table_if_not_exists()
            self.create_cart()
        except sqlite3.Error as e:
            print(f"Error: {e}")


    def create_cart(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cartitems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    price TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def create_table_if_not_exists(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT,
                    lastname TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def add_tocart(self, cartitem):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO cartitems (title, price)
                VALUES (?, ?)
            ''', (cartitem.title,cartitem.price))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
   

    def add_user(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO users (firstname, lastname, email, password)
                VALUES (?, ?, ?, ?)
            ''', (user.get_first_name(), user.get_last_name(), user.get_email(), user.get_password()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def user_exists(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            user = cursor.fetchone()
            return user is not None
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False

    def get_user_by_email(self, email):
      try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            user_data = cursor.fetchone()
            if user_data:
             id, first_name, last_name, email, password = user_data
             return User(first_name, last_name, email, password)
            else:
             print("User not found in the database.")
            return None
      except sqlite3.Error as e:
        print(f"Error: {e}")
        return 
        
    def deletecartitem(self, id):
      try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM cartitems WHERE id=?", (id,))
             
            return None
      except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

    def getcartitems(self):
      try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM cartitems")
            cartdata=cursor.fetchall()

            for data in cartdata:
                print(data[1])
                print(data[2])
             
            # while cursor.fetchall.Next():
            #     print()
            
            return cartdata
      except sqlite3.Error as e:
        print(f"Error: {e}")
        return None


    def close_connection(self):
        if self.conn:
            self.conn.close()

# # Example usage:
# if __name__ == "__main__":
#     db_file = "mydatabase.db"
#     user_manager = UserManager(db_file)

#     # Example: Creating and adding a new user
#     new_user = User("John", "Doe", "john@example.com", "password123")
#     user_manager.add_user(new_user)

#     # Example: Checking if a user exists
#     if user_manager.user_exists("john@example.com"):
#         print("User exists")
#     else:
#         print("User does not exist")

#     # Example: Retrieving a user by email
#     retrieved_user = user_manager.get_user_by_email("john@example.com")
#     if retrieved_user:
#         print("User found:", retrieved_user.get_first_name())
#     else:
#         print("User not found")

#     # Close the database connection when done
#     user_manager.close_connection()
