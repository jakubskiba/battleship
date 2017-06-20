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
    X hit
    O miss
  - Text appropriate representation of the element

* hit(self)
  - Returns None
  - Change is_hit attribute to True
