import sqlite3

# The problem will create a database named usersdata if it does not exist yet

connection = sqlite3.connect("usersdata.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    email TEXT,
    username TEXT,
    password_1 TEXT,
    password_2 TEXT
);
""")

option = 0
while option != 1 and option != 2:
    option = int(input("Choose an option:\n[1] Create an account\n[2] Login\n"))

if option == 1:
    email = input("Enter your e-mail address: ")
    username = input("Choose an username: ")
    while True:

        # If the program is able to find the username chosen in the database, it will not give any error

        try:
            cursor.execute(f"""
                    SELECT * FROM users
                    WHERE username = "{username}"
                    """)
            print("\033[31mUsername already in use")
            username = input("Choose an username: \033[m")
        except:
            break
    password_1v1 = input("Enter the first password: ")
    password_1v2 = input("Confirm your first password: ")
    while password_1v1 != password_1v2:
        print("\033[31m[ERROR] The confirmation do not match with the original password")
        password_1v1 = input("Enter the first password: ")
        password_1v2 = input("Confirm your first password: \033[m")
    password_2v1 = input("Enter the second password: ")
    password_2v2 = input("Confirm your second password: ")
    while password_2v1 != password_2v2:
        print("\033[31m[ERROR] The confirmation do not match with the original password")
        password_2v1 = input("Enter your second password: ")
        password_2v2 = input("Confirm your second password: \033[m")
    cursor.execute(f'INSERT INTO users VALUES ("{email}", "{username}", "{password_1v1}", "{password_2v1}")')
else:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cursor.execute(f"""
        SELECT * FROM users
        WHERE username = "{username}"
        """)

    """
    The row is a list with all the database rows with the chosen username. In this case, only one row
    will have the desired username, so the program will pick the first item index (0) and the password_1 and
    password_2 indexes (2, 3, respectively)
    """

    row = cursor.fetchall()
    if row[0][2] == password or row[0][3] == password:
        print("\033[32m[ACCESS ACCEPTED]\033[m")


connection.commit()
connection.close()
