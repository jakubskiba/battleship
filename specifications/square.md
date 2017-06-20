# SQUARE

## THE CLASS DESCRIPTION

Single element of the ocean

__Attributes__
* 'row'
  - data: int
  - description: y coordinate

* 'column'
  - data: int
  - description: x coordinate

* 'state'
  - data: str
  - description:
    - "~" unhit water
    - " " hit water
    - "o" unhit ship part
    - "x" hit ship part

__Methods__
* __init__(self, row, column)
  - Returns None
  - Description: Constructor method for element

* __str__(self)
  - Returns string
    ~ water or hidden part of ship
    X hit ship part
    O unhit ship part
   " " hit water
  - Text appropriate representation of the element

* change_state(self, state)
  - Returns None
  - Change state attribute to given value
