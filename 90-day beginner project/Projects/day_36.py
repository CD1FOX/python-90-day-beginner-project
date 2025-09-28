def calculator(num1, num2, operator):
    if operator == 1:
        return num1+num2
    elif operator == 2:
        return num1-num2
    elif operator == 3:
        return num1*num2
    elif operator == 4:
        return num1/num2
    else:
        return "Error, please try again!"

while True:
    num1_input = int(input("Input first number: "))
    num2_input = int(input("Input second number: "))
    operator_input = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nInput Operator Number: "))

    print(calculator(num1_input, num2_input, operator_input))