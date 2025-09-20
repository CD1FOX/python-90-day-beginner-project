while True:
    print("Input averages\n")
    math_ave = int(input("Enter average in math: "))
    sci_ave = int(input("Enter average in science: "))
    filipino_ave = int(input("Enter average in filipino: "))

    total_average = (math_ave + sci_ave + filipino_ave) / 3
    print(f"The total average for the {math_ave},{sci_ave} and {filipino_ave} is {int(total_average)}")