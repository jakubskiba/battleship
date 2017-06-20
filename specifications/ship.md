# SHIP

## THE CLASS DESCRIPTION

Object represents whole ship, compounded of squares objects

__Attributes__
* squares
  - data: list
  - description: list of squares contained in the ship

* 'length'
  - data: int
  - description: number of squares contained in the ship

* 'start_row'
  - data: int
  - description: y coordinate of ships stern

* 'start_column'
  - data: int
  - description: x coordinate of ships stern

* 'is_sunk'
  - data: bool
  - description: True if sunk

* 'name'
  - data: str
  - description: type of the ship

* 'is_vertical'
  - data: bool
  - description: True if ship is vertical

* 'is_hit'
  - data:bool
  - description: True if all ship squares are hit



__Methods__
* __init__(self, star_row, start_column, name, is_vertical)
  - Returns None
  - Description: Constructor method for element

* get_ship_length(self)
  - Returns int

* get_ship_name(self)
  - Returns: str
  - Description: gets names of the ship from their length

* generate_ship(self)
  - Returns: None
  - Description: creates and appends square objects to the squares list

* __str__(self)
  - Returns: string
  - Description: Text representation of the element
