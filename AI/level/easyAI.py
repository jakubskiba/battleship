import random

from AI.level.abstractAI import AbstractAI


class EasyAI(AbstractAI):
    def __init__(self, game):
        super().__init__(game)

    def draw_location_to_hit(self):
        """
        Generate which coordinates should be typed as a candidate to hit by algorithm.
        """
        row_num = random.randint(0, len(self.enemy_board[0]) - 1)
        column_num = random.randint(0, len(self.enemy_board[0]) - 1)
        if self.enemy_board[row_num][column_num].can_be_hit():
            return row_num, column_num
