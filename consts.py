from enum import Enum


class Direction(int, Enum):
    NORTH = 0
    NORTH_EAST = 1
    EAST = 2
    EAST_SOUTH = 3
    SOUTH = 4
    SOUTH_WEST = 5
    WEST = 6
    WEST_NORTH = 7

    @staticmethod
    def anti_clockwise(d):
        if d > 0:
            return d - 1

        return Direction.WEST_NORTH

    @staticmethod
    def clockwise(d):
        if d < 7:
            return d + 1

        return Direction.NORTH

    @staticmethod
    def opposite(d):
        return (d + 4) % 8

    @staticmethod
    def is_opposite(d1, d2):
        return Direction.opposite(d1) == d2

    @staticmethod
    def is_clockwise(d1, d2):
        return Direction.clockwise(d1) == d2

    @staticmethod
    def is_anti_clockwise(d1, d2):
        return Direction.anti_clockwise(d1) == d2

    def __int__(self):
        return self.value

    @staticmethod
    def rotation_cost(d1, d2):
        diff = abs(d1 - d2)
        return min(diff, 8 - diff)

    @staticmethod
    def rotation_angle(d1, d2):# rotation angle from d1->d2, the value could be negative;
        if d1 <= d2:
            r = d2 - d1
            if r >= 4:
                return -(8 - r)
            else:
                return r
        else:
            r = d1 - d2
            if r > 4:
                return (8 - r)
            else:
                return -r


MOVE_DIRECTION = [
    (1, 0, Direction.EAST),
    (-1, 0, Direction.WEST),
    (0, 1, Direction.NORTH),
    (0, -1, Direction.SOUTH),
    # (-1, -1, Direction.SOUTH_WEST),
    # (-1, 1, Direction.WEST_NORTH),
    # (1, 1, Direction.NORTH_EAST),
    # (1, -1, Direction.EAST_SOUTH),
]

TURN_FACTOR = 1

EXPANDED_CELL = 1 # for both agent and obstacles

AGENT_DIM = 3

WIDTH = 20
HEIGHT = 20

ITERATIONS = 2000
TURN_RADIUS = 1

SAFE_COST = 3 # the cost for the turn in case there is a chance that the robot is touch some obstacle
SCREENSHOT_COST = 5 # the cost for the place where the picture is taken