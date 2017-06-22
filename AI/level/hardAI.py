import random

from AI.level.abstractAI import AbstractAI

ODD_PATTERN = 1
EVEN_PATTERN = 2


class HardAI(AbstractAI):
    def __init__(self, last_hit):
        super().__init__()
        self.last_hit = last_hit

    def calculate_probability(self):
        hitable_squares = 0
        ship_squares = 0
        for row in self.enemy_board:
            for square in row:
                if square.state == "~":
                    hitable_squares += 1
                elif square.state == "□": # sprawdzić czy kwadrat jest statkiem
                    ship_squares += 1

        return ship_squares/hitable_squares

    def set_square_probability(self):
        for row in self.enemy_board:
            for square in row:
                square.probability = self.calculate_probability()

    def is_hit(self):
        pass