from AI.level.easyAI import EasyAI
from AI.level.normalAI import NormalAI
from AI.level.hardAI import HardAI

from AI.enum.enum import EASY as EASY
from AI.enum.enum import NORMAL as NORMAL
from AI.enum.enum import HARD as HARD


class ArtificialIntelligence:

    def __init__(self, difficulty_level, game):
        self.level = difficulty_level.level
        self.game = game
        self.mode = None
        self.set_mode()
        self.coordY, self.coordX = self.determine_where_to_hit()

    def set_mode(self):
        if self.level == EASY:
            self.mode = EasyAI(self.game)
        elif self.level == NORMAL:
            self.mode = NormalAI(self.game)
        elif self.level == HARD:
            self.mode = HardAI(self.game)

    def determine_where_to_hit(self):
        """
        Method to choose where to hit -> which depends on difficulty level.

        :returns
            tuple of coordinates (y, x)
        """
        hit_coordinates = None
        if self.level == EASY:
            hit_coordinates = self.mode.draw_location_to_hit()
        elif self.level == NORMAL:
            hit_coordinates = self.mode.draw_location_to_hit()
        elif self.level == HARD:
            self.mode.method_is_hit()
            if self.mode.hunting_mode:
                self.mode.ship_hunt()
                hit_coordinates = self.mode.draw_location_to_hit()
            else:
                hit_coordinates = self.mode.draw_location_to_hit()
        else:
            raise ValueError("Invalid difficulty level")
        return hit_coordinates
