import difficulty_level


class HitGenerator:
    def __init__(self):
        self.level = difficulty_level.DifficultyLevel()

    def generate_hit(self):
        if self.level == 1:
            easyAI.xxx()
        elif self.level == 2:
            normalAI.xxx()
        elif self.level == 3:
            hardAI.xxx()
        else:
            raise ValueError("Invalid level")
