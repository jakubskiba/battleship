from AI.artificial_intelligence import ArtificialIntelligence
from AI.difficulty_level import DifficultyLevel


def main():
    difficulty_level = DifficultyLevel()
    difficulty_level.set_level("normal")

    artificial_intelligence = ArtificialIntelligence(difficulty_level)
    hit_coordinates = artificial_intelligence.determine_where_to_hit()
    print(artificial_intelligence.__dict__)


if __name__ == "__main__":
    main()
