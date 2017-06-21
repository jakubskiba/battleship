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
        if name == 'computer':
            self.is_human = False
        else:
            self.is_human = True
        self.my_turn = False

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

    