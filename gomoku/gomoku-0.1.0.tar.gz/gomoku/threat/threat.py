from enum import IntEnum
from .. utils import to_row

class ThreatType(IntEnum):
    # Five in a row.
    # o o o o o
    FIVE = 5
    # Four in a row with open ends.
    # - o o o o -
    STRAIGHT_FOUR = 4
    # Four pieces in a line of 5 squares.
    # x o o o o -
    # x o o o - o
    # o o - o o x
    FOUR = 3
    # Three pieces in a row.
    # - o o o -
    THREE = 2
    # Three pieces in a line of 5 squares that aren't in a row.
    # - o o - o -
    # - o - o o -
    BROKEN_THREE = 1


class Threat:
    def __init__(self, gain=-1, cost=[], rest=[], inc=-1, type=None):
        '''Threat representation.

        Parameters
        ----------
        gain: index of 'gain' square.
            The gain square is the square played by the attacker.
            In this example of a three threat:
                - - o - o - -
                      ^
            The middle unoccupied square is the gain square.
        cost: list of 'cost' squares.
            Cost squares are squares played by the defender in response to a threat, excepting the gain square.
            The following are cost squares to a three threat.
                v   v

            - - o - o - -
              ^       ^
            The middle square is left out, as it is the gain square.
        rest: list of 'rest' squares.
            Rest squares are already played pieces that form the threat.
            The following are rest squares to a three threat.
                v   v
            - - o - o - -
            Those are
        b1 : bits of player 1.
        b2 : bits of player 2.
        turns: number of turns taken.
        '''
        self.type = type
        self.gain_square = gain
        self.cost_squares = cost
        self.rest_squares = rest
        self.inc = inc

    def __eq__(self, other):
        return self.gain_square == other.gain_square and self.cost_squares == other.cost_squares and self.rest_squares == other.rest_squares

    def __hash__(self):
        return hash((self.type, self.gain_square, 'cost', *self.cost_squares, 'rest', *self.rest_squares))

    def __str__(self):
        return (
            f'type: {self.type.name:<14}'
            f'gain: {str(to_row(self.gain_square)):<10}'
            f'cost: {str([to_row(s) for s in self.cost_squares]):<30}'
            f'rest: {str([to_row(s) for s in self.rest_squares]):<30}'
        )

class BrokenThree(Threat):
    def __init__(self, gain, cost, rest, inc):
        super().__init__(gain, cost, rest, inc, type=ThreatType.BROKEN_THREE)

class Three(Threat):
    def __init__(self, gain, cost, rest, inc):
        super().__init__(gain, cost, rest, inc, type=ThreatType.THREE)

class Five(Threat):
    def __init__(self, initial, inc, gain):
        super().__init__(inc=inc, type=ThreatType.FIVE)
        self.gain_square = gain
        self.rest_squares = [i for i in range(initial, initial + 5 * inc, inc) if i != gain]

class Four(Threat):
    def __init__(self, initial, inc, gain, cost):
        super().__init__(inc=inc, type=ThreatType.FOUR)
        self.gain_square = gain
        self.rest_squares = [i for i in range(initial, initial + 5 * inc, inc) if i != gain and i != cost]
        self.cost_squares = [cost]

class StraightFour(Four):
    def __init__(self, initial, inc, gain, cost):
        super().__init__(initial, inc, gain, cost)
        self.type = ThreatType.STRAIGHT_FOUR
