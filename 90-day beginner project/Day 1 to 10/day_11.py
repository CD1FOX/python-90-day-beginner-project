import random

num = random.randint(1, 100)

while True:
    print(num)
    guess = int(input("Guess a number between 1 and 100: "))

    if num == guess:
        print("Correct!")
    elif num < guess:
        print("Too high!")
    elif num > guess:
        print("Too low!")
    else:
        print("Not in the range")