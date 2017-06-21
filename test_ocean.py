from ocean import *
o = Ocean()
o.generate_board()
o.is_owner_looking = True
o.generate_ships()
print(o.ships)
print(o)