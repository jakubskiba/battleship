from ocean import Ocean
from game import Game
import random

ODD_PATTERN = 1
EVEN_PATTERN = 2


class AbstractAI:
    def __init__(self, game):
        self.my_board = None
        self.enemy_board = None
        self.set_board(game)        # Setter for current player boards.
        self.last_target = None
        self.is_hit = False
        self.taken_hits = []
        self.possible_hits = []
        self.hunting_mode = False
        self.ship_number = 5
        self.pattern_type = self.draw_pattern_type()

    def set_board(self, game):
        if game.players.get("first").name == "computer":

            self.my_board = game.players.get("first").ocean.board
            self.enemy_board = game.players.get("second").ocean.board
        elif game.players.get("second").name == "computer":
            self.my_board = game.players.get("second").ocean.board
            self.enemy_board = game.players.get("first").ocean.board

    @staticmethod
    def draw_pattern_type():
        """
        Generate what type of squares (odd / even) should be typed by algorithm.

        1. ODD PATTERN coordinates
        .---------.
        | |X| |X| | --> ([0, 1], [0, 3])
        |X| |X| |X| --> ([1, 0], [1, 2], [1, 4])
        | |X| |X| | --> ([2, 1], [2, 3])
        '---------'

        2. EVEN PATTERN coordinates
        .---------.
        |X| |X| |X| --> ([0, 0], [0, 2], [0, 4])
        | |X| |X| | --> ([1, 1], [1, 3])
        |X| |X| |X| --> ([2, 0], [2, 2], [2, 4])
        '---------'
        """
        return random.randint(ODD_PATTERN, EVEN_PATTERN)

    def draw_location_to_hit(self):
        """
        Generate which coordinates should be typed as a candidate to hit by algorithm.
        """
        row_num = random.randint(0, len(self.enemy_board[0]) - 1)
        column_num = random.randint(0, len(self.enemy_board[0]) - 1)
        return row_num, column_num

    @staticmethod
    def check_if_square_type_is_even(row_num, column_num):
        """
        Special method to check if square is 'odd' or 'even' type.

        KEY:
          modulo for sum of coordinates define the type of square.

          e.g.:     [0, 5] =     0 + 5 = 5     5 % 2 =     1
                                                           return: False  (not even)
        """
        if (row_num + column_num) % 2 == 0:
            return True
        else:
            return False

    def search_ship_algorithm(self):
        while True:
            row_num, column_num = self.draw_location_to_hit()
            if self.pattern_type == EVEN_PATTERN and self.check_if_square_type_is_even(row_num, column_num):
                return row_num, column_num
            elif self.pattern_type == ODD_PATTERN and not self.check_if_square_type_is_even(row_num, column_num):
                return row_num, column_num
            else:
                continue

    def toggle_hunting_mode(self, game):
        counter = 5
        for ship in game.players.get("first").ocean.ships:
            if ship.is_sunk:
                counter -= 1
        if counter < self.ship_number:
            self.ship_number = counter
            self.hunting_mode = False
        else:
            self.hunting_mode = True
