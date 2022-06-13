import random


options = {
    'R': 'Rock',
    'S': 'Scissors',
    'P': 'Paper'
    }

print('=========================')
print('ROCK PAPER SCISSORS GAME')
print('=========================\n')

def play():
    user_choice = None
    computer_choice = None
    winner = None
    is_playing = True

    while is_playing:
        computer_choice = random.choice(list(options))
        # random.choice, to help us pick a random item from a list
        user_choice = input('To play, pick between R, S or P\nTo cancel press X\n')

        if user_choice == 'X':
            print('Good bye!!!')
            is_playing = False
            continue 
        # go to the next loop iteration and stop, because <is_playing> is now False,
        # necessary to avoid an endless loop.

        if user_choice not in options:
            print('Error: Wrong input!!!')
            play()
        print(f'Player ({options[user_choice]}) : CPU ({options[computer_choice]})')

    # Checking both moves
        if user_choice == computer_choice:
            print('The game is a DRAW\n')
            play()
        elif user_choice == 'R' and computer_choice == 'S':
            winner = 'You'
        elif user_choice == 'S' and computer_choice == 'P':
            winner = 'You'
        elif user_choice == 'P' and computer_choice == 'R':
            winner = 'You'
        elif user_choice == 'S' and computer_choice == 'R':
            winner = 'Computer'
        elif user_choice == 'P' and computer_choice == 'S':
            winner = 'Computer'
        elif user_choice == 'R' and computer_choice == 'P':
            winner = 'Computer'
        else:
            continue
        # declare the winner
        print(f'{winner} wins!!!')
        print()
        play()  # starts the game all over again!

play()