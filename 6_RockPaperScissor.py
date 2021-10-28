print("\n**~**~**~~**:>Welcome to RPS Game<:**~**~**~~**\n")

player1: str = input("Enter player-1 name : ")
player2: str = input("Enter player-2 name : ")

choice = 'yes'

while choice == 'yes':

    print("\nGet ready to play......\n")

    p1 = input(player1 + " -----> Choose rock/paper/scissor : ")
    p2 = input(player2 + " -----> Choose rock/paper/scissor : ")

    if p1 == p2:
        print("Its a draw game!!!")

    elif p1 == 'rock':
        if p2 == 'scissor':
            print("Player-1",player1, "wins!!!")
        elif p2 == 'paper':
            print("Player-2",player2, "wins!!!")
        else:
            print("\nOOPSE!!! Invalid input, try again!!!")


    elif p1 == 'scissor':
        if p2 == 'paper':
            print("Player-1",player1, "wins!!!")
        elif p2 == 'rock':
            print("Player-2",player2, "wins!!!")
        else:
            print("\nOOPSE!!! Invalid input, try again!!!")

    elif p1 == 'paper':
        if p2 == 'rock':
            print("Player-1",player1, "wins!!!")
        elif p2 == 'scissor':
            print("Player-2",player2, "wins!!!")
        else:
            print("\nOOPSE!!! Invalid input, try again!!!")

    else:
        print("\nOOPSE!!! Invalid input, try again!!!")

    choice = input("\nWant to play again? (Yes/No): ")

