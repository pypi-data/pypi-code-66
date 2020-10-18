import random
from collections import Counter
from .. threat.threat_search import get_fives, get_fours, get_threes
from .. threat.threat_space import threat_space_search
from .. threat.threat import ThreatType
from .. utils import to_row

VERBOSE=1


class Negamax:
    def negamax(self, b, depth=2, multiplier=1):
        print(b)
        if depth <= 0:
            # print(threat_space_search(b))
            if threat_space_search(b):
                return 1
            return 0

        val = -1000
        moves = []
        for move in [tup[1] for tup in self.score_moves(b)][:5]:
            _b = b.copy()
            _b.move_index(move)
            val = max(val, -self.negamax(_b, depth=depth-1, multiplier=-multiplier))
        return val


    def make_move(self, b):
        if b.turns == 0: return (7, 7)
        if b.turns == 1:
            if b.is_valid_move(7, 7): return (7, 7)
            return (6, 6)

        # make forced move
        forced = self.forced_moves(b)
        if forced:
            if VERBOSE: print(f'Making forced move...: {to_row(forced)}')
            return forced

        # search for winning line
        moves = threat_space_search(b, VERBOSE=VERBOSE)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(t.gain_square) for t in moves[0]]}')
            return moves[0][0].gain_square

        best_val = -1000
        best_move = None

        for move in [tup[1] for tup in self.score_moves(b)][:5]:
            _b = b.copy()
            _b.move_index(move)
            val = self.negamax(_b, multiplier=-1)
            if val > best_val:
                best_val = val
                best_move = move
        return best_move

    def score_moves(self, b, limit_moves=None):
        if not limit_moves:
            limit_moves = self.valid_moves(b)
        scored_moves = []
        for move in limit_moves:
            _b = b.copy()
            _b.force_index(move)
            score = 0
            score += len(get_fours(_b)) * 4 + len(get_threes(_b)) * 3
            score *= 1.5
            score -= len(get_fours(_b, current=False)) * 4 + len(get_threes(_b, current=False)) * 3
            scored_moves.append((score, move))
        scored_moves.sort(reverse=True)
        return scored_moves


    def valid_moves(self, b):
        # get all possible moves on the board
        moves = [
            r * 15 + c
            for r in range(b.size) for c in range(b.size)
            if b.is_valid_move(r, c)
        ]
        return moves

    def forced_moves(self, b):
        # make 5
        forced = get_fives(b)
        if forced: return forced[0].gain_square

        # block 5
        forced = get_fives(b, current=False)
        if forced: return forced[0].gain_square

        # make straight 4
        forced = [t for t in get_fours(b) if t.type == ThreatType.STRAIGHT_FOUR]
        if forced: return forced[0].gain_square

        return None
