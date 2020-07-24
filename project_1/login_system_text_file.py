import pickle


def get_users():
    """
    This function opens the users file, reads it and returns its content
    :return: A dictionary with details about the users
    """
    infile = open("users", 'rb')
    users = pickle.load(infile)
    infile.close()
    return users


try:
    users_dict = get_users()
except:
    # If the users file does not exist, the program will create it and insert an empty dictionary on it
    empty_dict = {"emails": list(), "usernames": list(), "passwords_1": list(), "passwords_2": list()}
    outfile = open("users", 'wb')
    pickle.dump(empty_dict, outfile)
    outfile.close()
    users_dict = get_users()

option = 0
while option != 1 and option != 2:
    option = int(input("Choose an option:\n[1] Create an account\n[2] Login\n"))

if option == 1:
    email = input("Enter your e-mail address: ")
    username = input("Choose an username: ")
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

    users_dict["emails"].append(email)
    users_dict["usernames"].append(username)
    users_dict["passwords_1"].append(password_1v1)
    users_dict["passwords_2"].append(password_2v1)

    outfile = open("users", 'wb')                           # Opens the users file in the writing mode
    pickle.dump(users_dict, outfile)                        # Updates the users file with the new user's information
    outfile.close()
else:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    index = users_dict["usernames"].index(username)
    while password != users_dict["passwords_1"][index] and password != users_dict["passwords_2"][index]:
        print("\033[31m[ACCESS DENIED] Your username and/or your password are wrong")
        username = input("Enter your username: ")
        password = input("Enter your password: \033[m")
    else:
        print("\033[32m[ACCESS ACCEPTED]\033[m")
