class Square:
    """
    Single element of the ocean

    Attributes:
        row (int)
        column (int)
        state (str)
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = '~'

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state

    def __is_change_possible(self, state):
        """
        Checks correctness of changes
        """

        if self.state == '~' and state == ' ':
            return True

        elif self.state == '~' and state == 'o':
            return True

        elif self.state == 'o' and state == 'x':
            return True
        else:
            return False

    def change_state(self, state):
        """
        Changes state attribute

        Args:
            state (str): new state
        """
        if self.__is_change_possible(state):
            self.state = state

        '''
        # proposed feature
            return True
        else:
            return False
        '''
