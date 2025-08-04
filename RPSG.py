import random


print ("Rock, Paper, Scissors Game")

user = input("choose rock, paper, scissors: ").lower().strip()
computer = random.choice(["rock", "paper", "scissors"])

print("you chose:", user)
print("computer chose:", computer)

wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
if user == computer:
    print("It's a Tie!!")
elif wins_against[user] == computer:
    print("You win!!")
else:
    print("You Lose!!")
