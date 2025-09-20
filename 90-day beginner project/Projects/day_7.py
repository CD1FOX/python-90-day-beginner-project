# Ask for a number
num = int(input("Enter a number: "))

# Print multiplication table (1–10)
print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
