from AI.artificial_intelligence import ArtificialIntelligence
from AI.difficulty_level import DifficultyLevel
from game import Game


def main():
    difficulty_level = DifficultyLevel("hard")
    difficulty_level.set_level("hard")
    game = Game()


    AI = ArtificialIntelligence(difficulty_level, game)

if __name__ == "__main__":
    main()
