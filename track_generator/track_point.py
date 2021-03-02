import math
class TrackPoint:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)

    # def distance(self, otherX: float, otherY: float):
    #     return math.sqrt(
    #         math.pow((self.x-otherX), 2)
    #         +
    #         math.pow((self.y-otherY),2))

