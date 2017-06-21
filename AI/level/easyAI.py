from AI.abstractAI import AbstractAI
import random


class EasyAI(AbstractAI):
    def __init__(self):
        super().__init__()

    def hit_location(self):
        row_num = random.randint(0, len(self.ocean.board[0])-1)
        column_num = random.randint(0, len(self.ocean.board[0])-1)
        if self.ocean.board[row_num][column_num].can_be_hit():
            return row_num, column_num
