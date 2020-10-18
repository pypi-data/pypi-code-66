from . import threat
from .. utils import get_ones
from . threat_masks import threat_mask

cached_threes = {}
cached_fours = {}
cached_fives = {}
cached_straight_fours = {}

def get_straight_fours(b, current=True):
    k = (b.b1, b.b2, current)
    if k not in cached_straight_fours:
        cached_straight_fours[k] = _get_straight_fours(b, current)
    return cached_straight_fours[k]

def get_fours(b, current=True):
    k = (b.b1, b.b2, current)
    if k not in cached_fours:
        cached_fours[k] = _get_fours(b, current)
    return cached_fours[k]

def get_fives(b, current=True):
    k = (b.b1, b.b2, current)
    if k not in cached_fives:
        cached_fives[k] = _get_fives(b, current)
    return cached_fives[k]

def get_threes(b, current=True):
    k = (b.b1, b.b2, current)
    if k not in cached_threes:
        cached_threes[k] = _get_threes(b, current)
    return cached_threes[k]

def get_threats(board, current=True):
    threats = get_fives(board, current=current) + get_fours(board, current=current) + get_threes(board, current=current)
    return threats

def _get_threes(board, current=True):
    # - - - o o - -
    # - - o - o - -
    # - - o o - - -
    straight_three_lookup = [
        [ [2], [0, 1, 2, 5, 6], [1, 5], [3, 4] ],
        [ [3], [0, 1, 3, 5, 6], [1, 5], [2, 4] ],
        [ [4], [0, 1, 4, 5, 6], [1, 5], [2, 3] ],
    ]

    # 12: - o o ! ? -
    # 13: - o ! o ? -
    # 14: - o ? ? o -
    # 23: - ! o o ! -
    # 24: - ? o ! o -
    # 34: - ? ! o o -
    three_lookup = [
        [ [3, 4], [0, 3, 4, 5], [1, 2], [4] ],
        [ [2, 4], [0, 2, 4, 5], [1, 3], [4] ],
        [ [2, 3], [0, 2, 3, 5], [1, 4], [2, 3] ],
        [ [1, 4], [0, 1, 4, 5], [2, 3], [] ],
        [ [1, 3], [0, 1, 3, 5], [2, 4], [1] ],
        [ [1, 2], [0, 1, 2, 5], [3, 4], [1] ],
    ]

    b = board.get_board(current=current)
    ret = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        cur = {}
        for gain, emp, cost, rest in straight_three_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2]) & (board.e >> inc * emp[3]) & (board.e >> inc * emp[4])
            bits = (b >> inc * rest[0]) & (b >> inc * rest[1])
            bits = bits & threat_mask[7][inc] & e_bits

            for o in get_ones(bits):
                gain_square = o + gain[0] * inc
                cur[gain_square] = threat.Three(
                    gain=gain_square,
                    cost=list([o + c * inc for c in cost]),
                    rest=list([o + c * inc for c in rest]),
                    inc=inc
                )

        for gains, emp, rest, broken in three_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2]) & (board.e >> inc * emp[3])
            bits = (b >> inc * rest[0]) & (b >> inc * rest[1])
            bits = bits & threat_mask[6][inc] & e_bits

            for o in get_ones(bits):
                for i, gain in enumerate(gains):
                    gain_square = o + gain * inc
                    cost_square = o + gains[i - 1] * inc
                    if gain_square not in cur:
                        threat_type = threat.ThreatType.BROKEN_THREE if gain in broken else threat.ThreatType.THREE

                        cur[gain_square] = threat.Threat(
                            gain=gain_square,
                            cost=[o, o + inc * 5, cost_square],
                            rest=[o + r * inc for r in rest],
                            inc=inc,
                            type=threat_type,
                        )
        ret += cur.values()
    return ret

def _get_straight_fours(board, current=True):
    b = board.get_board(current=current)
    ret = []
    ################
    # STRAIGHT FOURS
    ################
    # - ! o o o -
    # - o ! o o -
    # - o o ! o -
    # - o o o ! -
    straight_four_lookup = [
        [ [0, 1, 5], [2, 3, 4] ],
        [ [0, 2, 5], [1, 3, 4] ],
        [ [0, 3, 5], [1, 2, 4] ],
        [ [0, 4, 5], [1, 2, 3] ],
    ]

    for inc in [1, board.size, board.size + 1, board.size - 1]:
        for emp, occ in straight_four_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2])
            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2])
            bits = bits & threat_mask[6][inc] & e_bits

            for o in get_ones(bits):
                ret.append(threat.StraightFour(o, inc, o + inc * emp[1], o))
    return ret

def _get_fours(board, current=True):
    b = board.get_board(current=current)
    ret = []

    ################
    # FOURS
    ################
    # 01: - - o o o
    # 02: - o - o o
    # 03: - o o - o
    # 04: - o o o -

    # 12: o - - o o
    # 13: o - o - o
    # 14: o - o o -

    # 23: o o - - o
    # 24: o o - o -

    # 34: o o o - -
    four_lookup = [
        [ [0, 1], [2, 3, 4] ],
        [ [0, 2], [1, 3, 4] ],
        [ [0, 3], [1, 2, 4] ],
        [ [0, 4], [1, 2, 3] ],
        [ [1, 2], [0, 3, 4] ],
        [ [1, 3], [0, 2, 4] ],
        [ [1, 4], [0, 2, 3] ],
        [ [2, 3], [0, 1, 4] ],
        [ [2, 4], [0, 1, 3] ],
        [ [3, 4], [0, 1, 2] ],
    ]

    # add straight_fours
    sfs = get_straight_fours(board, current)
    sf_set = set()
    for t in sfs:
        sf_set.add((t.gain_square, t.inc))
    ret += sfs

    for inc in [1, board.size, board.size + 1, board.size - 1]:
        for emp, occ in four_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1])
            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2])
            bits = bits & threat_mask[5][inc] & e_bits
            for o in get_ones(bits):
                i1 = o + emp[0] * inc
                i2 = o + emp[1] * inc
                if (i1, inc) not in sf_set:
                    ret.append(threat.Four(o, inc, i1, i2))
                if (i2, inc) not in sf_set:
                    ret.append(threat.Four(o, inc, i2, i1))
    return ret

def _get_fives(board, current=True):
    b = board.get_board(current=current)
    ret = []

    # 0: - o o o o
    # 1: o - o o o
    # 2: o o - o o
    # 3: o o o - o
    # 4: o o o o -
    lookup = [
        [ [0], [1, 2, 3, 4] ],
        [ [1], [0, 2, 3, 4] ],
        [ [2], [0, 1, 3, 4] ],
        [ [3], [0, 1, 2, 4] ],
        [ [4], [0, 1, 2, 3] ],
    ]

    for inc in [1, board.size, board.size + 1, board.size - 1]:
        for emp, occ in lookup:
            e_bits = (board.e >> inc * emp[0])
            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2]) & (b >> inc * occ[3])
            bits = bits & threat_mask[5][inc] & e_bits
            for o in get_ones(bits):
                ret.append(threat.Five(o, inc, o + emp[0] * inc))
    return ret

def has_five(board, current=True):
    '''Returns True if current player has a 5 in a row.'''
    b = board.get_board(current=current)
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        bits = b & (b >> inc) & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
        bits = bits & threat_mask[5][inc]
        if bits: return True
    return False
