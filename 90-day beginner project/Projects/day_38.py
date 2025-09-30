# ATM Simulator (Basic)

def atm_simulator():
    balance = 1000  # starting balance
    while True:
        print("\n===== ATM Simulator =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            print(f"\nYour current balance is: ₱{balance}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"₱{amount} deposited successfully.")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                elif amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    balance -= amount
                    print(f"₱{amount} withdrawn successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


# Run the ATM
atm_simulator()
