import time

from AI.level.abstractAI import AbstractAI
import random

ODD_PATTERN = 1
EVEN_PATTERN = 2


class HardAI(AbstractAI):
    def __init__(self, game):
        super().__init__(game)

    def draw_location_to_hit(self):
        """
        Generate which coordinates should be typed as a candidate to hit by algorithm.
        """
        row_num = random.randint(0, len(self.enemy_board[0]) - 1)
        column_num = random.randint(0, len(self.enemy_board[0]) - 1)
        if self.is_hit:
            self.ship_hunt()
        return row_num, column_num

    def calculate_probability(self):
        hittable_squares = 0
        ship_squares = 0
        for row in self.enemy_board:
            for square in row:
                if square.state == "~":
                    hittable_squares += 1
                elif square.state == "□":
                    ship_squares += 1

        return ship_squares/hittable_squares

    def set_square_probability(self):
        for row in self.enemy_board:
            for square in row:
                square.probability = self.calculate_probability()

    def check_is_hit(self):
        row_num, column_num = self.search_ship_algorithm()
        if self.enemy_board[row_num][column_num].state == "□":
            self.last_target = row_num, column_num
            self.is_hit = True
            self.hunting_mode = True

    def ship_hunt(self):
        water = "~"
        row_num, column_num = self.last_target
        print(self.last_target)

        try:
            if self.enemy_board[row_num][column_num + 1].state == water:
                self.possible_hits.append((row_num, column_num + 1))
        except IndexError:
            pass

        try:
            if self.enemy_board[row_num][column_num - 1].state == water:
                self.possible_hits.append((row_num, column_num - 1))
        except IndexError:
            pass

        try:
            if self.enemy_board[row_num + 1][column_num].state == water:
                self.possible_hits.append((row_num + 1, column_num))
        except IndexError:
            pass

        try:
            if self.enemy_board[row_num - 1][column_num].state == water:
                self.possible_hits.append((row_num - 1, column_num))
        except IndexError:
            pass

        next_hit = random.randint(0, len(self.possible_hits) - 1)
        self.last_target = self.possible_hits[next_hit]

