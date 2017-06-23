from ocean import Ocean


class Player:
    """
    Attributes:
        name(str)
        ocean(obj)
        my_turn(bool)
    """

    def __init__(self, name='computer'):
        self.name = name
        self.ocean = Ocean()
        self.enemy_ocean = Ocean()
        self.my_turn = False

    @property
    def is_human(self):
        if self.name == 'computer':
            return False
        else:
            return True

    def count_unhited_squares(self):
        """
        Counts number of unhit squares

        Returns:
            int
        """

        amount = 0

        for ship in self.ocean.ships:
            for square in ship.squares:
                if square.state == '□':
                    amount += 1

        return amount

    def __str__(self):
        """
        Returns:
            (str)
        """
        if self.is_human:
            is_human = '(P)'
        else:
            is_human = '(C)'
        return 'name: ' + self.name + is_human
