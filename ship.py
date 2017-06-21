from square import Square


class Ship:
    def __init__(self, start_row, start_column, name, is_vertical):
        """
        Method creates an instance of the class

        Returns:
            None
        """

        self.name = name
        self.start_row = start_row
        self.start_column = start_column
        self.is_vertical = is_vertical
        self.length = self.get_ship_length()
        self.squares = []
        self.generate_ship()

    def get_ship_length(self):
        """
        Method returns ship length which depends on the name

        Returns:
            length (int): ship length
        """

        ship_lengths = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        length = ship_lengths[self.name]
        return length

    def generate_ship(self):
        """
        Method creates objects of Square class and appends them to the list

        Returns:
            None
        """

        for i in range(self.length):
            if self.is_vertical:
                self.squares.append(Square(self.start_row + i, self.start_column))
            else:
                self.squares.append(Square(self.start_row, self.start_column + i))
            self.squares[-1].change_state('□')

    @property
    def is_hit(self):
        for square in self.squares:
            if square.state == 'X':
                return True
        return False

    @property
    def is_sunk(self):
        for square in self.squares:
            if square.state == '□':
                return False
        return True

    def __str__(self):
        """
        Method overloads the str operator

        Returns:
            str_ship (str): string used by print function
        """

        str_ship = [square.state for square in self.squares]
        str_ship = ''.join(str_ship)
        return str_ship


def main():
    ship = Ship(3, 5, 'Carrier', True)
    print(ship)
    ship.squares[-3].change_state('x')
    print(ship)
    print(ship.is_hit)
    print(ship.is_sunk)
    for i in range(5):
        ship.squares[i].change_state('X')
    print(ship)
    print(ship.is_hit)
    print(ship.is_sunk)


if __name__ == '__main__':
    main()
