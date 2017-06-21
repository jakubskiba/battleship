from difficulty_level import DifficultyLevel
import easyAI

class HitGenerator:
    def __init__(self):
        self.level = DifficultyLevel()

    def generate_hit(self):
        if self.level == 1:
            easyAI
        elif self.level == 2:
            # normalAI.xxx()
        elif self.level == 3:
            # hardAI.xxx()
        else:
            raise ValueError("Invalid level")
