import random

from AI.level.abstractAI import AbstractAI


class EasyAI(AbstractAI):
    def __init__(self):
        super().__init__()

    def draw_location_to_hit(self):
        """
        Generate which coordinates should be typed as a candidate to hit by algorithm.
        """
        row_num = random.randint(0, len(self.ocean.board[0]) - 1)
        column_num = random.randint(0, len(self.ocean.board[0]) - 1)
        if self.ocean.board[row_num][column_num].can_be_hit():
            return row_num, column_num
