import random

from AI.level.abstractAI import AbstractAI

ODD_PATTERN = 1
EVEN_PATTERN = 2


class HardAI(AbstractAI):
    def __init__(self):
        super().__init__()

    def calculate_probability(self):
        hitable_squares = 0
        ship_squares = 0
        for row in self.ocean.board: # sprawdzić po ktorej planszy iterujemy
            for square in row:
                if square.state == "~":
                    hitable_squares += 1
                elif square.state == "□":
                    ship_squares += 1

        return ship_squares/hitable_squares

    def set_square_probability(self):
        for row in self.ocean.board:
            for square in row:
                square.probability = self.calculate_probability()