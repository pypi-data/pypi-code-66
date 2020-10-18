import random
from collections import Counter
from .. threat.threat_search import get_fives, get_fours, get_threes
from .. threat.threat_space import threat_space_search
from .. threat.threat import ThreatType
from .. utils import to_row

VERBOSE=1

class ThreatSpace:
    def __init__(self):
        self.winning_line = []

    def request_move(self, b, game):
        move = self.make_move(b)
        game.make_move(move)

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

    def valid_moves(self, b):
        return [i for i in range(225) if b.is_valid_index(i)]

    def make_move(self, b):
        # input("Press Enter to continue...")
        if b.turns == 0: return (7, 7)
        if b.turns == 1:
            if b.is_valid_move(7, 7): return (7, 7)
            return (6, 6)

        forced = self.forced_moves(b)
        if forced:
            if VERBOSE: print(f'Making forced move...: {to_row(forced)}')
            self.winning_line = []
            return forced

        if self.winning_line:
            if VERBOSE: print(f'Saved winning line being played: {[to_row(t.gain_square) for t in self.winning_line[::-1]]}')
            return self.winning_line.pop().gain_square

        # search for winning line
        moves = threat_space_search(b, VERBOSE=VERBOSE)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(t.gain_square) for t in moves[0]]}')
            self.winning_line = moves[0][::-1]
            return self.winning_line.pop().gain_square
        else:
            if VERBOSE: print(f'Winning line not found...')

        # # search for winning line in opponent's board
        moves = threat_space_search(b, current=False, max_seqs=1, VERBOSE=VERBOSE)
        limit_moves = None
        if not moves:
            print('Enemy winning line not found...')
        elif moves:
            for seq in moves:
                workable_moves = set()
                if VERBOSE: print(f'Enemy winning seq------------')
                for t in seq:
                    workable_moves.add(t.gain_square)
                    if t.type == ThreatType.STRAIGHT_FOUR:
                        workable_moves.update([sq for sq in t.rest_squares if b.is_valid_index(sq)])
                        workable_moves.add(t.rest_squares[0] - t.inc)
                        workable_moves.add(t.rest_squares[2] + t.inc)
                    else:
                        workable_moves.update(t.cost_squares)

                    if VERBOSE: print(str(t))

                if limit_moves is None:
                    limit_moves = workable_moves
                else:
                    limit_moves = limit_moves & workable_moves

            if VERBOSE: print(f'Moves limited to: {[to_row(move) for move in limit_moves]}')

        # make a move based on simple heuristic
        score_moves = self.score_moves(b, limit_moves=limit_moves)
        best_moves = [tup[1] for tup in score_moves][:10]
        threatening_moves = Counter()
        for move in best_moves:
            _b = b.copy()
            _b.force_index(move)
            if VERBOSE: print(f'Searching {to_row(move)}')

            tss = threat_space_search(_b, VERBOSE=VERBOSE, current=False)
            if tss:
                if VERBOSE: print(f'{to_row(move)} allows the opponent to win with seq: {[to_row(t.gain_square) for t in tss[0]]}, skipping...')
                continue

            # TODO: if no threatening, sort by terminated_nodes
            tss = threat_space_search(_b, VERBOSE=VERBOSE)
            if tss:
                moves = [move]
                [moves.append(t.gain_square) for t in tss[0]]
                if VERBOSE: print(f'Threatening line: {[to_row(t) for t in moves]}')
                for move in moves:
                    threatening_moves[move] += 1

        if threatening_moves:
            best_threatening = [(v, k) for k, v in threatening_moves.items() if k in best_moves]
            best_threatening.sort(reverse=True)
            if VERBOSE: print(f'Best threatening moves: {best_threatening}')
            return best_threatening[0][1]
        if VERBOSE: print('Random move...')
        return random.choice(best_moves[:3])
