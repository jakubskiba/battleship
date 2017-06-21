class Game:
    def __init__(self):
        """
        Method creates an instance of the class

        Returns:
            None
        """

        self.players = {"first": Player(), "second": Player()}

    def check_whose_turn(self):
        """
        Method checks both objects of class Player and returns Player with attribute my_turn = True

        Returns:
            obj of class Player
        """

        for key in self.players:
            if self.players[key].my_turn:
                return self.players[key]

    def switch_turn(self):
        """
        Method switches both players my_turn attributes to opposed

        Returns:
            None
        """

        for key in self.players:
            self.players[key].my_turn = not my_turn


def main():
    pass


if __name__ == '__main__':
    main()
