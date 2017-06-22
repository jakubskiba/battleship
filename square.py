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

    def change_state(self, state):
        """
        Changes state attribute

        Args:
            state (str): new state
        """

        self.state = state

    def hit(self):
        """
        """

        possible_changes = {'~': 'O', '□': 'X'}
        hit_messages = {'~': 'Miss!', '□': 'Hit!'}

        message = hit_messages[self.state]
        self.state = possible_changes[self.state]
        return message

    def can_be_hit(self):
        if self.state in ['~', '□']:
            return True
        else:
            return False
