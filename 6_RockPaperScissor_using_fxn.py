print("\n**~**~**~~**:>Welcome to RPS Game<:**~**~**~~**\n")

player1: str = input("Enter player-1 name : ")
player2: str = input("Enter player-2 name : ")

print("\nGet ready to play................")

choice = 'yes'


def user_choice():
    cont = str(input('\nWant to play again? (Yes/No): '))
    return cont


def compare(p1, p2):

    if p1 == p2:
        print('Its a Draw!!!')

    if p1 == 'scissor' and p2 == 'rock':
        print('\nPlayer 2 <', player2, '> wins!!!')

    elif p2 == 'scissor' and p1 == 'rock':
        print('\nPlayer 1 <', player1, '> wins!!!')

    elif p1 == 'paper' and p2 == 'scissor':
        print('\nPlayer 2 <', player2, '> wins!!!')

    elif p2 == 'paper' and p1 == 'scissor':
        print('\nPlayer 1 <', player1, '> wins!!!')

    elif p1 == 'paper' and p2 == 'rock':
        print('\nPlayer 1 <', player1, '> wins!!!')

    elif p2 == 'paper' and p1 == 'rock':
        print('\nPlayer 2 <', player2, '> wins!!!')


while choice == 'yes':
    print()
    p1 = str(input(player1 + " -----> Choose rock/paper/scissor : "))
    p2 = str(input(player2 + " -----> Choose rock/paper/scissor : "))
    compare(p1, p2)
    choice = user_choice()

print("\n<><><><><><> Thank You For Playing <><><><><><>")
