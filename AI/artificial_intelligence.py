from AI.level.easyAI import EasyAI
from AI.level.normalAI import NormalAI


class ArtificialIntelligence:

    def __init__(self, level):
        position_y = 0
        position_x = 1

        self.level = level
        self.coordY = self.determine_where_to_hit()[position_y]
        self.coordX = self.determine_where_to_hit()[position_x]

    def determine_where_to_hit(self):
        """
        Method to choose where to hit -> which depends on difficulty level.

        :returns
            tuple of coordinates (y, x)
        """
        hit_coordinates = None

        if self.level == 1:
            hit_coordinates = EasyAI().draw_location_to_hit()
        elif self.level == 2:
            hit_coordinates = NormalAI().draw_location_to_hit()
        elif self.level == 3:
            pass
            # hardAI.xxx()
        else:
            raise ValueError("Invalid difficulty level")

        return hit_coordinates
