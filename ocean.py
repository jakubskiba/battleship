from square import Square
from ship import Ship
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

    def __check_square_availability(self, row, column):
        """
        Checks if it is possible to place square in specified coordinates
        """

        for y in range(-1, 2):
            for x in range(-1, 2):
                try:
                    if str(self.board[row + y - 1][column + x - 1]) != '~':
                        return False
                except IndexError:
                    continue
        return True

    def check_possibility_of_ship_placement(self, ship):
        """
        Simulates placement of each square of ship, if succeed makes real replacement

        Returns:
            (bool)
        """

        for ship_square in ship.squares:
            try:
                board_square = self.board[ship_square.row - 1][ship_square.column - 1]
            except IndexError:
                return False

            if self.__check_square_availability(board_square.row, board_square.column):
                continue
            else:
                return False
        return True

    def place_ship_on_board(self, new_ship):
        """
        Places provided ship on board
        """

        for i in range(len(new_ship.squares)):
            row = new_ship.squares[i].row - 1
            column = new_ship.squares[i].column - 1
            self.board[row][column] = new_ship.squares[i]

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
                    board += '~ '
                else:
                    board += current_square + ' '
            board += str(row + 1) + '\n'
        return board
