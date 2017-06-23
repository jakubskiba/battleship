from game import Game

from AI.level.abstractAI import AbstractAI


class NormalAI(AbstractAI):
    def __init__(self, game):
        super().__init__(game)
