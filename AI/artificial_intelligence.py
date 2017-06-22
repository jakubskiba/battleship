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
        self.coordY, self.coordX = self.determine_where_to_hit(game)

    def set_mode(self):
        if self.level == EASY:
            self.mode = EasyAI(self.game)
        elif self.level == NORMAL:
            self.mode = NormalAI(self.game)
        elif self.level == HARD:
            self.mode = HardAI(self.game)

    def determine_where_to_hit(self, game):
        """determine_where_to_hit
        Method to choose where to hit -> which depends on difficulty level.

        :returns
            tuple of coordinates (y, x)
        """
        hit_coordinates = None
        if self.level == EASY:
            hit_coordinates = self.mode.draw_location_to_hit()
        elif self.level == NORMAL:
            hit_coordinates = self.mode.search_ship_algorithm()
        elif self.level == HARD:
            self.mode.check_is_hit()
            if self.mode.hunting_mode:
                self.mode.ship_hunt()
                self.mode.toggle_hunting_mode(game)
                hit_coordinates = self.mode.search_ship_algorithm()
            else:
                hit_coordinates = self.mode.search_ship_algorithm()
        else:
            raise ValueError("Invalid difficulty level")
        return hit_coordinates
