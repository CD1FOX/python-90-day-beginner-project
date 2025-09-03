# Ask the user for the bill amount
bill_amount = float(input("What is the total bill amount? "))

# Ask the user for the tip percentage
tip_percentage = int(input("What percentage would you like to tip? (e.g., 15, 20) "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount
total_amount = bill_amount + tip_amount

# Print the results
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total bill with tip: ${total_amount:.2f}")