import time
from .. threat.threat_search import get_fives, get_fours, get_threats, has_five, get_straight_fours
from .. threat.threat import ThreatType

threat_space_cache = {}

def confirm_winning_line(b, threats):
    '''Confirms if a string of threats leads to a win.

    Parameters
    ----------
    b: current board.
    threats: array of threats leading to a supposed win.
    '''
    # base case
    if len(threats) == 0: return True

    t = threats[0]

    # if we have a win, return True.
    if get_fives(b): return True
    # if the enemy has a five threat we must counter that disrupts our threat chain, return False
    if [f for f in get_fives(b, current=False) if f.gain_square != t.gain_square]: return False

    # place the gain square of the first threat
    b.force_index(t.gain_square)

    # if we aren't threatening to win the very next turn...
    if t.type < ThreatType.FOUR:
        # if the enemy has a straight four threat and the threat we executed is less than 4, we lose
        if get_straight_fours(b, current=False): return False
        # TODO: check if sf.gain_square != t.gain_square is necessary
        # if [sf for sf in get_straight_fours(b, current=False) if sf.gain_square != t.gain_square]: return False

        # now we need to play out all the opponents' normal fours.
        opponent_fours = get_fours(b, current=False)
        if opponent_fours:
            processed_fours = set()

            # for each four that has not been played yet, play every other legal four.
            for ot in opponent_fours:
                if ot in processed_fours:
                    continue
                _b = b.copy()
                for ot1 in opponent_fours:
                    if _b.is_valid_index(ot1.gain_square) and _b.is_valid_index(ot1.cost_squares[0]):
                        processed_fours.add(ot1)
                        _b.force_index(ot1.gain_square)
                        _b.force_index(ot1.cost_squares[0], current=False)

                # after playing all fours, undo our threat's gain square and see if we still have a winning line.
                _b.force_undo_index(t.gain_square)
                if not confirm_winning_line(_b, threats): return False
            return True

    # the only moves the opponent can make are:
    # moves that directly block the incoming threat
    # five threats IF we aren't threatening a five
    for cs in t.cost_squares:
        _b = b.copy()
        _b.force_index(cs, current=False)
        if not confirm_winning_line(_b, threats[1:]): return False
    return True

def threat_space_search(b, current=True, depth=7, max_seqs=1, VERBOSE=0):
    '''Implementation of Victor Allis's threat space search.

    Parameters
    ----------
    b: current board.
    current: whether to search the threat space of the current player or the other player
    depth: how deep to search
    max_seqs: maximum number of winning threat sequences we should look for.
    VERBOSE: whether to print out debugging information/statistics
    '''
    nodes = 0
    terminated_nodes = 0
    execs = 0
    original = b.copy()
    seqs = []
    def _search(b, moves=[], current=True, depth=10):
        '''Recursive helper function.

        Parameters
        ----------
        moves: array of threats currently being searched.
        '''
        nonlocal nodes
        nonlocal terminated_nodes
        nonlocal execs

        from .. utils import to_row

        if depth <= 0:
            terminated_nodes += 1
            return

        # get threats
        threats = get_threats(b, current=current)

        # return if winning threat is found
        if has_five(b):
            if confirm_winning_line(original.copy(), moves):
                seqs.append(moves)
                return
        for t in threats:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR:
                if confirm_winning_line(original.copy(), [*moves, t]):
                    seqs.append([*moves, t])
                    return

        # search all dependent threats
        # dependent threats are threats whose gain square lies in the rest squares of our previous threat
        # if moves is empty, consider all threats
        if moves:
            dependent = [t for t in threats if moves[-1].gain_square in t.rest_squares]
        else:
            dependent = threats

        for t in dependent:
            # play gain square, play all cost squares
            _b = b.copy()
            _b.force_index(t.gain_square, current=current)
            [_b.force_index(cost, current=not current) for cost in t.cost_squares]

            _search(_b, moves=[*moves, t], current=current, depth=depth-1)
            if len(seqs) >= max_seqs: return


        # search all independent threats
        # independent threats are threats whose gain squares combine to form another threat
        inline = set([1, 2, 15, 30, 16, 32, 14, 28])
        for i in range(len(threats)):
            for j in range(i + 1, len(threats)):
                t = threats[i]
                u = threats[j]

                # the combination of two threats should only be considered if:
                # 1. their gain squares lie in a line, and are close enough to each other
                # 2. the gain square of threat A does not lie in the cost squares of threat B, and vice versa.
                # TODO: investigate whether the inline set needs to be expanded for gaps of length 2
                if abs(t.gain_square - u.gain_square) in inline and t.gain_square not in u.cost_squares and u.gain_square not in t.cost_squares and set(u.cost_squares).isdisjoint(t.cost_squares):
                    # play both threats, then search the board with depth-2.
                    _b = b.copy()
                    _b.force_index(t.gain_square, current=current)
                    [_b.force_index(cost, current=not current) for cost in t.cost_squares]

                    _b.force_index(u.gain_square, current=current)
                    [_b.force_index(cost, current=not current) for cost in u.cost_squares]

                    _search(_b, moves=[*moves, t, u], current=current, depth=depth-2)
                    if len(seqs) >= max_seqs: return
        nodes += 1
        execs += 1

    s = time.time()
    _search(b, moves=[], current=current, depth=depth)
    e = time.time()
    if VERBOSE: print(f'nodes: {nodes}, terminated_nodes: {terminated_nodes}, execs: {execs}, elapsed: {e - s}, {repr(original)}')
    return seqs
