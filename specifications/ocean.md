# OCEAN

## THE CLASS DESCRIPTION

Object represents whole game board for one player

__Attributes__
* ships
  - data: list
  - description: list of ships

* board
 - data: list
 - description: list of every square of the board

* is_owner_looking
 - data: bool
 - description: affects on the text representation of the board


__Methods__
* __init__(self)
  - Returns None
  - Description: Constructor method for the board
        generates board list of square objects
        generates ships list and append square objects to their square list

* generate_board(self)
  - Returns none
  - Description: generates board list of square objects

* check_possibility_of_ship_placement(self, ship)
  - Returns bool
  - Description: Simulates placement of each square of ship, if succeed makes real replacement

* place_ship_on_board(self, new_ship)
  - Returns none
  - Description: Places provided ship on board

* end_game(self)
  - Returns: bool
  - Description: True if every ship (of one player) is sunk

* __str__(self)
  - Returns: string
  - Description: Text representation of the board, depends on the player
