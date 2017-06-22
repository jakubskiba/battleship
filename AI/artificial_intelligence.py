from AI.level.easyAI import EasyAI
from AI.level.normalAI import NormalAI

from AI.enum.enum import EASY as EASY
from AI.enum.enum import NORMAL as NORMAL
from AI.enum.enum import HARD as HARD

POSITION_Y = 0
POSITION_X = 1


class ArtificialIntelligence:

    def __init__(self, difficulty_level):

        self.level = difficulty_level.level
        self.coordY = self.determine_where_to_hit()[POSITION_Y]
        self.coordX = self.determine_where_to_hit()[POSITION_X]

    def determine_where_to_hit(self):
        """determine_where_to_hit
        Method to choose where to hit -> which depends on difficulty level.

        :returns
            tuple of coordinates (y, x)
        """
        hit_coordinates = None

        if self.level == EASY:
            hit_coordinates = EasyAI().draw_location_to_hit()
        elif self.level == NORMAL:
            hit_coordinates = NormalAI().draw_location_to_hit()
        elif self.level == HARD:
            pass
            # hardAI.xxx()
        else:
            raise ValueError("Invalid difficulty level")

        return hit_coordinates
