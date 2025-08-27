def main():
    try:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("❌ Please enter valid numbers!")

if __name__ == "__main__":
    main()
