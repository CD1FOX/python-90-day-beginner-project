def password_strength(password):
    digits = 0
    letters = 0
    specials = 0

    for char in password:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            specials += 1

    print(f"Password: {password}")
    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Special characters: {specials}")

    # Simple strength evaluation
    if len(password) < 6:
        print("Strength: Weak (too short)")
    elif letters > 0 and digits > 0 and specials > 0 and len(password) >= 8:
        print("Strength: Strong")
    elif letters > 0 and digits > 0:
        print("Strength: Medium")
    else:
        print("Strength: Weak")

# Example usage
pwd = input("Enter a password: ")
password_strength(pwd)
