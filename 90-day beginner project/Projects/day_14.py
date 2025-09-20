grade = int(input("Enter grade(1-99): "))

if 1 <= grade <= 99:
    if grade >= 98:
        print("With Highest Honors")
    elif grade >= 95:
        print("With High Honors")
    elif grade >= 90:
        print("With Honors")
    elif grade >= 75:
        print("Passed")
    else:
        print("Failed")
else:
    print("Not in the range")