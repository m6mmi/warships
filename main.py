# Warships game
# Legend
# A - Aircraft carrier - 5 spaces
# B - Battleship - 4 spaces
# C - Cruiser - 3 spaces
# D - Destroyer - 2 spaces
# S - Submarine - 1 space
# X for a hit
# ' ' for empty space
# - for a miss

from main_functions import *

# Create the boards for the player and the enemy.
enemy_board_hidden = [[' '] * 8 for x in range(8)]
enemy_board = [[' '] * 8 for y in range(8)]
player_board = [[' '] * 8 for z in range(8)]


# Ask user input and check if it is valid. Return the coordinates
def user_choice():
    user_input = input('Please enter attack coordinates e.g. B2: ').upper()
    # Check if user input is valid
    while len(user_input) != 2 or user_input[0] not in 'ABCDEFGH' or user_input[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        user_input = input('Please enter attack coordinates e.g. B2: ').upper()
    colum = user_input[0]
    row = user_input[1]
    print(f'You attack! {colum}{row}', end=' ')
    return colum, row


# Randomly choose coordinates for the enemy. The Enemy cannot attack the same place twice. Return the coordinates
def enemy_choice():
    # Dict to convert letters to numbers
    letter_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    # Randomly choose coordinates
    colum, row = choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']), randint(1, 8)
    # Check if the coordinates are not occupied by X or
    while (player_board[int(row) - 1][letter_to_numbers[colum]] == f'{BackColors.red}X{BackColors.default}'
           or player_board[int(row) - 1][letter_to_numbers[colum]] == f'{BackColors.dark_blue}-{BackColors.default}'):
        colum, row = choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']), randint(1, 8)
    print(f'Enemy attack! {colum}{row}', end=' ')
    return colum, row


# Greet player
print('\nWelcome to the game of warships!\n')
print('  A - Aircraft carrier   B - Battleship\n'
      '  C - Cruiser            D - Destroyer\n'
      '  S - Submarine\n\n'
      '  X for a hit            - for a miss')
# Create ships
create_ships(player_board)
create_ships(enemy_board)
# Print boards
print_board(player_board, enemy_board_hidden)

# Main loop
while True:
    # Player attack
    attack(enemy_board, *user_choice(), hidden_board=enemy_board_hidden)
    # Enemy attack
    attack(player_board, *enemy_choice())
    # Print boards
    print_board(player_board, enemy_board_hidden)
    # Check for win
    if check_for_win(player_board, enemy_board):
        break
