from ocean import Ocean
from AI.abstractAI import AbstractAI
import random


class EasyAI(AbstractAI):
    def __init__(self):
        super().__init__()

    def hit_location(self):
        row_num = random.randint(1, len(self.board.board[0]))
        column_num = random.randint(1, len(self.board.board[0]))
        return row_num, column_num