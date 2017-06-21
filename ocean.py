from square import *
from ship import *
from copy import deepcopy


class Ocean:
    """
    Object represents whole game board for one player

    Attributes:
        ships(dict): dictionary of ships
            key(str): ship name
            value(obj): object of class Ship
        board(list): list of every square of the board
        is_owner_looking(bool): affects on the text representation of the board
    """

    def __init__(self):
        self.ships = []
        self.board = []
        self.is_owner_looking = False
        self.generate_board()

    def generate_board(self):
        """
        Generates board list of square objects

        Returns:
            None
        """

        for row in range(1, 11):
            column_list = []
            for column in range(1, 11):
                new_square = Square(row, column)
                column_list.append(new_square)
            self.board.append(column_list)

    def __generate_single_ship(self, ships_name):
        """
        Asks user for data
            Ship (obj)
        """

        row = ''
        while not (row.isdigit() and int(row) >= 1 and int(row) <= 10):
            row = input('Provide row for ' + ships_name + ':')
        row = int(row)

        column = ''
        while not (column.isdigit() and int(column) >= 1 and int(column) <= 10):
            column = input('Provide column for ' + ships_name + ':')
        column = int(column)

        is_vertical = input('Is ship vertical? (y or n)')
        while is_vertical != 'y' and is_vertical != 'n':
            is_vertical = input('Is ship vertical? (y or n)')
        if is_vertical == 'y':
            is_vertical = True
        else:
            is_vertical = False

        return Ship(row, column, ships_name, is_vertical)

    def __check_square_availability(self, row, column):
        """
            Checks if it is possible to place square in specified coordinates
        """

        for y in range(-1, 1):
            for x in range(-1, 1):
                try:
                    if str(self.board[row + y - 1][column + x - 1]) != '~':
                        return False
                except IndexError:
                    continue
        return True

    def __replace_squares(self, ship):
        """
            Simulates placement of each square of ship, if succeed makes real replacement

            Returns:
                (bool)
        """

        board = deepcopy(self.board)
        for ship_square in ship.squares:
            try:
                board_square = board[ship_square.row - 1][ship_square.column - 1]
            except IndexError:
                return False
            if self.__check_square_availability(board_square.row, board_square.column):
                board[ship_square.row - 1][ship_square.column - 1] = ship_square
            else:
                return False
        self.board = board
        return True

    def generate_ships(self):
        """
        Generates ships list, check correctness of ship placement and replace squares in board list

        Returns:
            None
        """
        ships_names = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        for ship_name in ships_names:
            print(self)
            ship_placed = False
            while not ship_placed:
                new_ship = self.__generate_single_ship(ship_name)
                ship_placed = self.__replace_squares(new_ship)
            self.ships.append(new_ship)

    def end_game(self):
        """
            Checks that each ship is sunk
            Returns:
                (bool)
        """

        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True

    def __str__(self):
        column_indexes = [chr(i) for i in range(65, 75)]
        first_row = ' '.join(column_indexes) + '\n'
        board = first_row
        for row in range(10):
            for column in range(10):
                current_square = str(self.board[row][column])
                if current_square == '□' and not self.is_owner_looking:
                    board += '~'
                else:
                    board += current_square + ' '
            board += str(row + 1) + '\n'
        return board
