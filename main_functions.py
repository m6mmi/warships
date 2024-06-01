from random import randint, choice


# Colors
class BackColors:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    grey = '\033[90m'
    orange = '\033[33m'
    dark_blue = '\033[34m'
    default = '\033[0m'


def place_ship(board, ship_length, symbol, color=BackColors.default):
    """ Function to place ships on the board. Checks if the ship can be placed and if so, place it on board. """
    while True:
        # Randomly choose orientation
        orientation = choice(['horizontal', 'vertical'])
        # Randomly choose coordinates
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        # Check if ship can be placed
        if orientation == 'horizontal' and ship_column + ship_length < 8:
            if [board[ship_row][i] for i in range(ship_column, ship_column + ship_length)] == [' '] * ship_length:
                for i in range(ship_length):
                    board[ship_row][ship_column + i] = f'{color}{symbol}{BackColors.default}'
                return
        elif orientation == 'vertical' and ship_row + ship_length < 8:
            if [board[ship_row + i][ship_column] for i in range(ship_length)] == [' '] * ship_length:
                for i in range(ship_length):
                    board[ship_row + i][ship_column] = f'{color}{symbol}{BackColors.default}'
                return


def create_ships(board):
    """ Function to create ships on the board. """
    place_ship(board, 5, 'A', color=BackColors.purple)
    place_ship(board, 4, 'B', color=BackColors.blue)
    place_ship(board, 3, 'C', color=BackColors.cyan)
    place_ship(board, 2, 'D', color=BackColors.orange)
    place_ship(board, 1, 'S', color=BackColors.grey)


def print_board(board_1, board_2):
    """  Function to print the boards. """
    print('-' * 50)
    print('     Player board                 Enemy board')
    print(f'{BackColors.yellow}   A B C D E F G H              A B C D E F G H{BackColors.default}')
    row_number = 1
    for row_1, row_2 in zip(board_1, board_2):
        print(f'{BackColors.green}{row_number:2}{BackColors.default}|{"|".join(row_1)}|          '
              f'{BackColors.green}{row_number:2}{BackColors.default}|{"|".join(row_2)}|')
        row_number += 1
    print('-' * 50)


def attack(board, colum, row, hidden_board=None):
    """  Function to attack the enemy/player board. """
    letter_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    if board[int(row) - 1][letter_to_numbers[colum]] == ' ':
        board[int(row) - 1][letter_to_numbers[colum]] = f'{BackColors.dark_blue}-{BackColors.default}'
        if hidden_board is not None:
            hidden_board[int(row) - 1][letter_to_numbers[colum]] = f'{BackColors.dark_blue}-{BackColors.default}'
        print('Miss!')
    elif (board[int(row) - 1][letter_to_numbers[colum]] == f'{BackColors.red}X{BackColors.default}'
          or board[int(row) - 1][letter_to_numbers[colum]] == f'{BackColors.dark_blue}-{BackColors.default}'):
        print('You already attacked there!')
    else:
        board[int(row) - 1][letter_to_numbers[colum]] = f'{BackColors.red}X{BackColors.default}'
        if hidden_board is not None:
            hidden_board[int(row) - 1][letter_to_numbers[colum]] = f'{BackColors.red}X{BackColors.default}'
        print('Hit!')


def check_for_win(player, enemy):
    """  Function to check if either player has won or lost. """
    ship_set = set('ABCDS')
    # Check for enemy board
    if all(all(ship not in cell for cell in row) for row in enemy for ship in ship_set):
        print('You won!')
        return True

    # Check for player board
    elif all(all(ship not in cell for cell in row) for row in player for ship in ship_set):
        print('You lost!')
        return True

    return False  # Neither player nor enemy has lost yet
