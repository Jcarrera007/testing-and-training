player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")

options = ["rock", "paper", "scissors", "r", "p", "s"]
player1_score = 0
player2_score = 0

print("Rock, Paper, Scissors Game")

while player1_score < 2 and player2_score < 2:
    player1 = None
    while player1 not in options:
        player1 = input("Player1, choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()

    player2 = None
    while player2 not in options:
        player2 = input("Player2, choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()

    print("Player 1 chose:", player1)
    print("Player 2 chose:", player2)

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
        print("Player 1 wins, Point 1 for Player 1!!")
        player1_score += 1
    else:
        print("Point for Player 2!!")
        player2_score += 1

    print("Score:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    print()

if player1_score == 2:
    print("Congratulations! Player 1 is the overall winner!")
else:
    print("Sorry! Player 2 is the overall winner!")

print("Game Over! Thanks for playing!")
