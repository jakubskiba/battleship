from AI.difficulty_level import DifficultyLevel
from AI.level.easyAI import EasyAI
from AI.level.normalAI import NormalAI


class ArtificialIntelligence:
    def __init__(self):
        self.level = DifficultyLevel()
        self.coordX = self.determine_where_to_hit()[0]
        self.coordY = self.determine_where_to_hit()[1]

    def determine_where_to_hit(self):
        """
        Method to choose where to hit -> which depends on difficulty level.
        """
        hit_coordinates = None

        if self.level == 1:
            hit_coordinates = EasyAI().draw_location_to_hit()
        elif self.level == 2:
            hit_coordinates = NormalAI().draw_location_to_hit()
        elif self.level == 3:
            pass
            # hardAI.xxx()
        else:
            raise ValueError("Invalid difficulty level")

        return hit_coordinates
