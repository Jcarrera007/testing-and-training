import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Rock, Paper, Scissors Game")

while player_score < 2 and computer_score < 2:
    player = None
    while player not in options:
        player = input("Choose rock, paper, scissors: ").lower()

    computer = random.choice(options)

    print("You chose:", player)
    print("Computer chose:", computer)

    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        print("It's a Tie!!")
    elif wins_against[player] == computer:
        print("You win, Point 1 for you!!")
        player_score += 1
    else:
        print("Point for computer!!")
        computer_score += 1

    print("Score:")
    print("You:", player_score)
    print("Computer:", computer_score)
    print()

if player_score == 2:
    print("Congratulations! You are the overall winner!")
else:
    print("Sorry! The computer is the overall winner!")

print("Game Over! Thanks for playing!")
