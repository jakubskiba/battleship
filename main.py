import os
import time
from game import Game
from ship import Ship
from random import randint, choice
from AI.artificial_intelligence import ArtificialIntelligence
from AI.difficulty_level import DifficultyLevel


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


def choose_ai_level():
    possible_ai = {'1': 'easy', '2': 'normal', '3': 'hard'}

    menu = '''
    1. easy
    2. normal
    3. hard
    '''
    print(menu)

    ai_level = ''
    while ai_level not in possible_ai:
        ai_level = input('Choose AI level: ')
    return possible_ai[ai_level]


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


def randomize_players_order():
    """
    Returns:
        (str)
    """
    which_player = randint(1, 2)
    if which_player == 1:
        return 'first'
    else:
        return 'second'


def get_shot_coordinates_from_user():
    """
    Ask user for shot coordinates

    Returns:
        coordinates(tuple)
            row(int): 0-9
            column(int): 0-9
    """

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


def get_coordinates(game, artificial_intelligence):
    """
    Switches shot coordinates input

    Returns:
        coordinates(tuple)
            row(int): 0-9
            column(int): 0-9
    """

    if game.get_operating_player().is_human:
        row, column = get_shot_coordinates_from_user()
    else:
        row, column = artificial_intelligence.determine_where_to_hit()

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
    Asks user for ships details

    Returns
        Ship (obj)

    """

    row = ask_user_for_row(ship_name)
    column = ask_user_for_column(ship_name)

    is_vertical = ask_user_is_ship_vertical()

    return Ship(row, column, ship_name, is_vertical)


def ask_user_for_ships(ocean):
    """
    Creates ships from user input

    Args:
        ocean(obj): Ocean object
    """

    ships_names = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    print(ocean)
    for ship_name in ships_names:
        new_ship = generate_single_ship(ship_name)
        while not ocean.check_possibility_of_ship_placement(new_ship):
            new_ship = generate_single_ship(ship_name)
        ocean.ships.append(new_ship)
        ocean.place_ship_on_board(new_ship)
        print(ocean)


def randomize_single_ship(ship_name):
    """
    Creates random ship
    """

    row = randint(1, 10)
    column = randint(1, 10)
    is_vertical = choice([False, True])
    new_ship = Ship(row, column, ship_name, is_vertical)

    return new_ship


def randomize_ships(ocean):
    """
    Places ships randomly
    """

    ships_names = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    for ship_name in ships_names:
        new_ship = randomize_single_ship(ship_name)
        while not ocean.check_possibility_of_ship_placement(new_ship):
            new_ship = randomize_single_ship(ship_name)
        ocean.ships.append(new_ship)
        ocean.place_ship_on_board(new_ship)


def intro(file_name):
    """Function displays intro image.

    Args:
        file_name: name of the file with image art
    """

    color = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    reset_color = '\033[0m'

    with open(file_name, 'r') as img_file:
        images = img_file.read()

    os.system('clear')
    print(images)


def read_highscore_file():
    """
    Returns:
        list of strings
            'points number: player name'
    """

    highscores = []

    FILE_PATH = 'additional_files/hall_of_fame.csv'
    with open(FILE_PATH, 'r') as f:
        for line in f:
            highscores.append(line.replace('\n', ''))

    return sorted(highscores)


def append_highscore_file(highscores):
    """
    Writes highscore list to file

    Args:
        highscores(list)
    Return None
    """

    FILE_PATH = 'additional_files/hall_of_fame.csv'
    with open(FILE_PATH, 'r+') as f:
        for highscore in highscores:
            f.write(highscore+'\n')


def update_highscore(win_player, lost_player):
    """
    Places current game score in highscores and call append_highscore_file function

    Args:
        win_player(obj): player object
        lost_player(obj): player object
    """

    score = str(win_player.count_unhited_squares())
    highscores = read_highscore_file()
    is_added = False
    for i in range(len(highscores)):
        highscore = highscores[i].split(':')[0]
        if int(score) > int(highscore):
            message = score + ': ' + win_player.name + ' won versus ' + lost_player.name
            highscores.insert(i, message)
            is_added = True
            break

    if not is_added:
        highscores.append(score + ': ' + win_player.name)

    append_highscore_file(highscores)


def print_highscore():
    """
    Print 10 lines of hall of fame file
    """

    os.system('clear')
    print('HALL OF FAME')
    print(' ' + '_' * 61)
    print('|{:>30}|{:>30}|'.format('winner', 'unhited squares').replace(' ', '_'))
    highscores = read_highscore_file()
    for highscore in highscores[:10]:
        highscore = highscore.split(': ')
        print('|{:>30}|{:>30}|'.format(highscore[1], highscore[0]).replace(' ', '_'))

    input('Press any key')


def placing_ships(current_player, waiting_player):
    """
    Switches between placing ships by human and computer
    """

    current_player.ocean.is_owner_looking = True
    print(current_player.name, 'set your ships!')
    if current_player.is_human:
        ask_user_for_ships(current_player.ocean)
    else:
        randomize_ships(current_player.ocean)

    os.system('clear')

    waiting_player.ocean.is_owner_looking = True
    print(waiting_player.name, 'set your ships!')
    if waiting_player.is_human:
        ask_user_for_ships(waiting_player.ocean)
    else:
        randomize_ships(waiting_player.ocean)


def print_turn_separator(current_player, waiting_player, game_mode):
    """
    Prints Press any key message

    Returns:
        None
    """

    if current_player.is_human and waiting_player.is_human:
        input('Press ENTER to continue')
        os.system('clear')
        intro('additional_files/cutscene.txt')
        print('Press ENTER to continue ' + waiting_player.name)
        input()
    if current_player.is_human and not waiting_player.is_human:
        input('Press ENTER to continue')

    if game_mode == 'CvC':
        time.sleep(0.1)
        os.system('clear')


def setup_game():
    game_mode = choose_game_mode()

    ai_level = 'easy'
    if game_mode != 'PvP':
        ai_level = choose_ai_level()

    game = Game()
    set_players_names(game, game_mode)

    difficulty_level = DifficultyLevel()
    difficulty_level.set_level(ai_level)

    artificial_intelligence = ArtificialIntelligence(difficulty_level)

    starting_player = randomize_players_order()
    game.players[starting_player].my_turn = True

    waiting_player = game.get_waiting_player()
    current_player = game.get_operating_player()

    os.system('clear')

    # placing ships
    placing_ships(current_player, waiting_player)

    return game, current_player, waiting_player, artificial_intelligence, game_mode


def main():
    print_highscore()
    intro('additional_files/intro_art.txt')

    game, current_player, waiting_player, artificial_intelligence, game_mode = setup_game()

    while not current_player.ocean.end_game():
        # game main loop

        current_player.ocean.is_owner_looking = True
        waiting_player.ocean.is_owner_looking = False

        os.system('clear')

        print(game)
        row, column = get_coordinates(game, artificial_intelligence)
        while not waiting_player.ocean.board[row][column].can_be_hit():
            row, column = get_coordinates(game, artificial_intelligence)

        message = waiting_player.ocean.board[row][column].hit()

        os.system('clear')
        print(game)

        set_and_print_hit_info(message, waiting_player, row, column)

        print_turn_separator(current_player, waiting_player, game_mode)

        game.switch_turn()
        waiting_player = game.get_waiting_player()
        current_player = game.get_operating_player()

    print('Congratulations!', waiting_player.name, 'won!')
    input('Press any key')
    update_highscore(waiting_player, current_player)
    print_highscore()


if __name__ == '__main__':
    main()
