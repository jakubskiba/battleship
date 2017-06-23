# PLAYER

## THE CLASS DESCRIPTION

Object represents one of the players

__Attributes__
* 'name'
  - data: string
  - description: player's name (default = 'computer')

* 'oceans'
  - data: dict
  - description: dictionary in form:
        - key: owner's name
        - value: ocean object

* 'my_turn'
    - data: bool
    - description: True if this player turn

* 'is_human'
    - data: bool
    - description: True if player is human

__Methods__
* __init__(self, name)
  - Returns None
  - Description: Constructor method for element

* __str__(self)
  - Returns string
  - Name
  
* count_unhited_quares(self)
  - Returns int
  - Count number of unhit squares