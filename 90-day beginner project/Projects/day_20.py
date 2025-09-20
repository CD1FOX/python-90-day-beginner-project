while True:
    user = "cd1fox"
    password = "lolmontage1221"

    user_input = input("What is your user?: ")
    password_input = input("What is your password?: ")

    if user == user_input and password == password_input:
        print("Welcome " + user + "!")
    else:
        print("Sorry " + user + "!")
