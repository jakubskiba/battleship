from ocean import Ocean


class AbstractAI:
    def __init__(self, game):
        self.my_board = None
        self.enemy_board = None
        self.set_board(self.my_board, self.enemy_board, game)

    def set_board(self, my_board, enemy_board, game):
        if game.players.get("first").name == "computer":
            game.players.get("first").ocean = my_board
            game.players.get("first").enemy_ocean = enemy_board
        elif game.players.get("second").name == "computer":
            game.players.get("second").ocean = my_board
            game.players.get("second").enemy_ocean = enemy_board

    def draw_location_to_hit(self):
        pass
