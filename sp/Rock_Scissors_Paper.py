# rock paper scissors
import random
while True:
    player = int(input("Your choice(1-rock, 2-scissors, 3-paper, 4-Quit): "))
    if player == 4:
        print("Exit the game.")
        break
    else:
        choices = {1: "rock", 2: "scissors", 3: "paper"}
        print(f"Your choice: {choices[player]}")
        computer = int(random.randint(1, 3))
        print(f"Computer choice: {choices[computer]}")
        
        if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            print("Player wins")
        elif player == computer:
            print("Draw")
        else:
            print("Computer wins")