import random
def game():
    return random.choice(["stone","paper","scissors"])
def play():
    print("Rock,Paper,Scissors shoot!")
    player1=game()
    player2=game()

    print(f"player 1 chose:{player1}")
    print(f"player 2 chose:{player2}")

    if player1=="stone" and player2=="paper":
        print("player 2 wins")
    elif player1=="stone" and player2=="scissor":
        print("player 1 wins")
    elif player1=="paper" and player2=="stone":
        print("player 1 wins")
    elif player1=="paper" and player2=="scissors":
        print("player 2 wins")
    elif player1=="scissors" and player2=="stone":
        print("player 2 wins")
    elif player1=="scissors" and player2=="paper":
        print("player 1 wins")
    else:
        print("tie")

