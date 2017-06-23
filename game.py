from player import Player


class Game:
    def __init__(self):
        """
        Method creates an instance of the class

        Returns:
            None
        """

        self.players = {"first": Player(), "second": Player()}

    def get_operating_player(self):
        """
        Method checks both objects of class Player and returns Player with attribute my_turn = True

        Returns:
            obj of class Player
        """

        for key in self.players:
            if self.players[key].my_turn:
                return self.players[key]

    def get_waiting_player(self):
        """
        Method checks both objects of class Player and returns Player with attribute my_turn = False

        Returns:
            obj of class Player
        """

        for key in self.players:
            if not self.players[key].my_turn:
                return self.players[key]

    def switch_turn(self):
        """
        Method switches both players my_turn attributes to opposed

        Returns:
            None
        """

        for key in self.players:
            self.players[key].my_turn = not self.players[key].my_turn

    def __str__(self):
        """
        Method overloads the str operator

        Returns:
            str_ship (str): string used by print function
        """

        current_player = self.get_operating_player()
        waiting_player = self.get_waiting_player()

        names_row = current_player.name + (31 - len(current_player.name)) * ' ' + waiting_player.name + '\n'

        current_str_board = current_player.ocean.__str__().splitlines()
        current_str_board = [line.strip() for line in current_str_board]
        next_str_board = waiting_player.ocean.__str__().splitlines()

        spaces = {0: 12, 10: 9}
        spaces.update({i: 10 for i in range(1, 10)})
        whole_game_view = [current_str_board[i] + spaces[i] * ' ' + next_str_board[i] for i in range(11)]
        whole_game_view = names_row + '\n'.join(whole_game_view)

        reset_color = '\033[0m'
        whole_game_view = whole_game_view.replace('□', '\033[31m' + '□' + reset_color)
        whole_game_view = whole_game_view.replace('~', '\033[34m' + '~' + reset_color)
        whole_game_view = whole_game_view.replace('X', '\033[33m' + 'X' + reset_color)
        whole_game_view = whole_game_view.replace('O', '\033[32m' + 'O' + reset_color)

        return whole_game_view


def main():
    pass


if __name__ == '__main__':
    main()
