match_password = "secret"

password = input("Enter a password: ").lower()
if password == match_password:
    print("It matched!")
else:
    print("It did not matched!")