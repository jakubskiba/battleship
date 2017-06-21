from AI.artificial_intelligence import ArtificialIntelligence
from AI.difficulty_level import DifficultyLevel


def main():
    difficulty_level = DifficultyLevel()
    difficulty_level.set_level("normal")

    artificial_intelligence = ArtificialIntelligence(difficulty_level.level)
    print(artificial_intelligence.level)

if __name__ == "__main__":
    main()
