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

* generate_boards(self)
  - Returns none
  - Description: generates board list of square objects

* generate_ships(self, ships_coordinates)
  - Returns: None
  - Description: generates ships list and append square objects to their square list

* generate_squares(self)
  - Returns: None
  - Description: creates and appends square objects to the squares list

* end_game(self)
  - Returns: bool
  - Description: True if every ship (of one player) is sunk

* __str__(self)
  - Returns: string
  - Description: Text representation of the board, depends on the player

