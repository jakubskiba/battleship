from AI.difficulty_level import DifficultyLevel
from AI.level import easyAI


class HitGenerator:
    def __init__(self):
        self.level = DifficultyLevel()
        self.coordX = self.generate_hit()[0]
        self.coordY = self.generate_hit()[1]

    def generate_hit(self):
        drawn_coordinates = None

        if self.level == 1:
            drawn_coordinates = easyAI.hit_location()
        elif self.level == 2:
            pass
            # normalAI.xxx()
        elif self.level == 3:
            pass
            # hardAI.xxx()
        else:
            raise ValueError("Invalid level")

        return drawn_coordinates
