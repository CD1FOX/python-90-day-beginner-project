word = input("Enter Word: ").lower()

if word == word[::-1]:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")