from AI.difficulty_level import DifficultyLevel
from AI.level.easyAI import EasyAI
from AI.level.normalAI import NormalAI


class ArtificialIntelligence:
    def __init__(self):
        self.level = DifficultyLevel()
        self.coordX = self.generate_hit()[0]
        self.coordY = self.generate_hit()[1]

    def generate_hit(self):
        drawn_coordinates = None

        if self.level == 1:
            drawn_coordinates = EasyAI().draw_location_to_hit()
        elif self.level == 2:
            drawn_coordinates = NormalAI().draw_location_to_hit()
        elif self.level == 3:
            pass
            # hardAI.xxx()
        else:
            raise ValueError("Invalid difficulty level")

        return drawn_coordinates
