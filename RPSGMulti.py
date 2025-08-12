print("Welcome to Rock ,Paper, Scissors!")
print("Lets Begin ...")
name1 = input("Player 1: What is your name? ")
name2 = input("Player 2: What is your name? ")
print("Hello " +name1 + " and " +name2)
print(name2 + ": Close your eyes!")

options = ["rock", "paper", "scissors", "r", "p", "s"]
player1_score = 0
player2_score = 0

while player1_score < 2 and player2_score < 2:
    player1 = None
    while player1 not in options:
        player1 = input(name1 + ", choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()

    player2 = None
    while player2 not in options:
        player2 = input(name2 + ", choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()

    print(name1 + " chose:", player1)
    print(name2 + " chose:", player2)

    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
        "r": "s",
        "s": "p",
        "p": "r"
    }

    if player1 == player2:
        print("It's a Tie!!")
    elif wins_against[player1] == player2:
        print(name1 + " wins!!")
        player1_score += 1
    else:
        print(name2 + " wins!!")
        player2_score += 1

    print("Score:")
    print(name1 + ":", player1_score)
    print(name2 + ":", player2_score)
    print()

if player1_score == 2:
    print("Congratulations! " + name1 + " is the overall winner!")
else:
    print("Sorry! " + name2 + " is the overall winner!")

print("Game Over! Thanks for playing!")
