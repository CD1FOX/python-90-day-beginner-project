import random

player_score = 0
computer_score = 0

choices = {1: "rock",
           2: "paper",
           3: "scissor"}

best_of_round_choice = {1: "Best of 3",
                        2: "Best of 5",
                        3: "Best of 7"}

while True:
    best_of_rounds = int(input("Please enter the number of best rounds: \n"
                               "1. Best of 3\n"
                               "2. Best of 5\n"
                               "3. Best of 7\n"
                               ">> "))

    difficulty = int(input("Enter difficulty:\n"
                           ""
                           "1. Easy Mode\n"
                           "2. Medium Mode\n"
                           "3. Hard Mode\n"
                           ">> "))

    player_choice = int(input("Choose one\n"
                              "1. Rock\n"
                              "2. Paper\n"
                              "3. Scissor\n"
                              ">> "))

    computer_choice = 0
    if difficulty == 1:
        computer_choice = random.randint(1, 3)
    elif difficulty == 2:
        if random.random() < 0.3:
            if player_choice == 1:
                computer_choice = 2
            elif player_choice == 2:
                computer_choice = 3
            elif player_choice == 3:
                computer_choice = 1
        else:
            computer_choice = random.randint(1, 3)
    elif difficulty == 3:
        if player_choice == 1:
            computer_choice = 2
        elif player_choice == 2:
            computer_choice = 3
        elif player_choice == 3:
            computer_choice = 1

    print(f"AI Choose {choices[computer_choice]}")
    print(f"Player Choose {choices[player_choice]}")

    if player_choice == computer_choice:
        print("TIE\n")
    elif player_choice == 1:
        if computer_choice == 2:
            print("YOU LOSE\n")
            computer_score += 1
        elif computer_choice == 3:
            print("YOU WIN\n")
            player_score += 1
    elif player_choice == 2:
        if computer_choice == 1:
            print("YOU WIN\n")
            player_score += 1
        elif computer_choice == 3:
            print("YOU LOSE\n")
            computer_score += 1
    elif player_choice == 3:
        if computer_choice == 1:
            print("YOU LOSE\n")
            computer_score += 1
        elif computer_choice == 2:
            print("YOU WIN\n")
            player_score += 1

    print(f"{best_of_round_choice[best_of_rounds]} round, current score:\n"
          f"player_score: {player_score}\n"
          f"computer_score: {computer_score}\n")



