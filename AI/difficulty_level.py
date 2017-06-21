class Difficulty_level:
    def __init__(self, name=""):
        self.name = name
        self.level = 1
        self.set_level(name)

    def set_level(self, name):
        if self.name == "easy":
            self.level = 1
        elif self.name == "normal":
            self.level = 2
        elif self.name == "hard":
            self.level = 3