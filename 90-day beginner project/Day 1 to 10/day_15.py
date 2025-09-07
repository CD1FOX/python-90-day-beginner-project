while True:
    year = int(input("Enter year(YYYY): "))

    if year % 4 == 0:
        print("Its a leap year")
    else:
        print("Not a leap year")