from AI.level.abstractAI import AbstractAI

ODD_PATTERN = 1
EVEN_PATTERN = 2


class HardAI(AbstractAI):
    def __init__(self, game):
        super().__init__(game)

    def calculate_probability(self):
        hittable_squares = 0
        ship_squares = 0
        for row in self.enemy_board:
            for square in row:
                if square.state == "~":
                    hittable_squares += 1
                elif square.state == "□": # sprawdzić czy kwadrat jest statkiem
                    ship_squares += 1

        return ship_squares/hittable_squares

    def set_square_probability(self):
        for row in self.enemy_board:
            for square in row:
                square.probability = self.calculate_probability()

    def is_hit(self):
        row_num, column_num = self.search_ship_algorithm()
        if self.enemy_board[row_num][column_num] == "□":
            self.last_target = row_num, column_num
            self.is_hit = True

