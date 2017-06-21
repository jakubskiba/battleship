class DifficultyLevel:
    def __init__(self, name=''):
        self.name = name
        self.level = None
        self.set_level(name)

    def set_level(self, name):
        if name == "easy":
            self.level = 1
        elif name == "normal":
            self.level = 2
        elif name == "hard":
            self.level = 3
