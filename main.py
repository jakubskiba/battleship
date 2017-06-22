from game import Game
from ship import Ship
from random import randint


def choose_game_mode():
    possible_modes = {'1': 'PvP', '2': 'PvC', '3': 'CvC'}
    menu = '''
    1. PvP
    2. PvC
    3. CvC
    '''
    print(menu)
    game_mode = ''
    while game_mode not in possible_modes:
        game_mode = input('Choose game mode: ')
    return possible_modes[game_mode]


def set_players_names(game, game_mode):
    """
    Returns:
        None
    """

    if game_mode == 'PvP':
        game.players['first'].name = input('Provide first player name: ')
        game.players['second'].name = input('Provide second player name: ')

    elif game_mode == 'PvC':
        game.players['first'].name = input('Provide first player name: ')

    elif game_mode == 'CvC':
        pass


def randomize_players_order():
    which_player = randint(1, 2)
    if which_player == 1:
        return 'first'
    else:
        return 'second'


def get_shot_coordinates_from_user():
    accepted_rows = [str(i) for i in range(1, 11)]
    accepted_columns = [chr(i) for i in range(65, 75)]

    row = ''
    while row not in accepted_rows:
        row = input('Please provide row (1-10): ')

    column = ''
    while column not in accepted_columns:
        column = input('Please provide column (A-J): ').upper()

    row = int(row) - 1

    column = ord(column) - 65

    return row, column


def get_shot_coordinates_from_AI():
    # INPUT AI HERE
    pass


def get_coordinates(game):
    """

    """
    if game.get_operating_player().is_human:
        row, column = get_shot_coordinates_from_user()
    else:
        row, column = get_shot_coordinates_from_AI()

    return row, column


def set_and_print_hit_info(message, waiting_player, row, column):
    print(message)
    if message == 'Hit!':
        for ship in waiting_player.ocean.ships:
            if waiting_player.ocean.board[row][column] in ship.squares and ship.is_sunk:
                print('Hit and sunk!')


def ask_user_for_row(ship_name):
    """
    Asks user for row until provided data aren't correct

    Returns:
        row(int)
    """

    accepted_rows = [str(i) for i in range(1, 11)]

    row = ''
    while row not in accepted_rows:
        row = input('Provide row for ' + ship_name + '[1 - 10]: ')
    return int(row)


def ask_user_for_column(ship_name):
    """
    Asks user for row until provided data aren't correct

    Returns:
        column(int)
    """

    accepted_columns = [chr(i) for i in range(65, 75)]

    column = ''
    while column not in accepted_columns:
        column = input('Provide column for ' + ship_name + '[A - J]: ').upper()
    return ord(column) - 64


def ask_user_is_ship_vertical():
    """
    Ask user for ship orientation

    Returns:
        bool
    """

    is_vertical = input('Is ship vertical? (y or n)')
    while is_vertical != 'y' and is_vertical != 'n':
        is_vertical = input('Is ship vertical? (y or n)')
    if is_vertical == 'y':
        is_vertical = True
    else:
        is_vertical = False

    return is_vertical


def generate_single_ship(ship_name):
    """
    Asks user for data

    Returns
        Ship (obj)

    """

    row = ask_user_for_row(ship_name)
    column = ask_user_for_column(ship_name)

    is_vertical = ask_user_is_ship_vertical()

    return Ship(row, column, ship_name, is_vertical)


def generate_ships(ocean):
    ships_names = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    print(ocean)
    for ship_name in ships_names:
        new_ship = generate_single_ship(ship_name)
        while not ocean.check_possibility_of_ship_placement(new_ship):
            new_ship = generate_single_ship(ship_name)
        ocean.ships.append(new_ship)
        ocean.place_ship_on_board(new_ship)
        print(ocean)


def main():
    game_mode = choose_game_mode()
    game = Game()
    set_players_names(game, game_mode)

    # set_ai_level()

    starting_player = randomize_players_order()
    game.players[starting_player].my_turn = True

    waiting_player = game.get_waiting_player()
    current_player = game.get_operating_player()

    # placing ships
    current_player.ocean.is_owner_looking = True
    print(current_player.name, 'set your ships!')
    generate_ships(current_player.ocean)

    waiting_player.ocean.is_owner_looking = True
    print(waiting_player.name, 'set your ships!')
    generate_ships(current_player.ocean)

    while not current_player.ocean.end_game():
        # game main loop

        current_player.ocean.is_owner_looking = True
        waiting_player.ocean.is_owner_looking = False
        print(game)
        row, column = get_coordinates(game)
        while not waiting_player.ocean.board[row][column].can_be_hit():
            row, column = get_coordinates(game)

        message = waiting_player.ocean.board[row][column].hit()
        set_and_print_hit_info(message, waiting_player, row, column)

        game.switch_turn()
        waiting_player = game.get_waiting_player()
        current_player = game.get_operating_player()


if __name__ == '__main__':
    main()
