def bmi_calculator(weight, height):
    return int(weight / height ** 2)


while True:
    weight = int(input("Enter weight in KG: "))
    height = int(input("Enter height in cm: "))

    meter_height = height / 100
    print(bmi_calculator(weight, meter_height))

