from game import Game
from random import randint


def choose_game_mode():
    possible_modes = {'1': 'PvP', '2': 'PvC', '3': 'CvC'}
    menu = '''1. PvP
    2. PvC
    3. CvC
    ''''
    print(menu)
    game_mode = ''
    while game_mode not in possible_modes:
        game_mode = input('Choose game mode: ')
    return possible_modes[game_mode]


def set_players_names(game_mode):
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
    if game.get_operating_player().is_human:
        row, column = get_shot_coordinates_from_user()
    else:
        row, column = get_shot_coordinates_from_AI()


def main():
    game_mode = choose_game_mode()
    game = Game()
    set_players_names(game_mode)

    # set_ai_level()

    starting_player = randomize_players_order()
    game.players[starting_player].my_turn = True

    waiting_player = game.get_waiting_player()
    current_player = game.get_operating_player()
    while not waiting_player.ocean.end_game():
        # tu dzieje się gra

        row, column = get_coordinates(game)
        while current_player.ocean.board[row][column]



        game.switch_turn()
        waiting_player = game.get_waiting_player()
        current_player = game.get_operating_player()


if __name__ == '__main__':
    main()