'''
Bitboard implementation.
Holds 2 integers, b1 and b2 for player 1 and player 2.
'''

import gmpy2

class Board:
    def __init__(self, b1=0, b2=0, turns=0):
        '''Bitboard instance.

        Parameters
        ----------
        b1 : bits of player 1.
        b2 : bits of player 2.
        turns: number of turns taken.
        '''
        self.b1 = b1
        self.b2 = b2
        self.turns = turns

        # hardcoded size of bitboard, 15x15.
        self.size = 15
        # bitmask of bitboard, 2**225 - 1
        self.mask = 53919893334301279589334030174039261347274288845081144962207220498431

        # represents bits occupied by either player.
        self.o = self.b1 | self.b2
        # represents bits not occupied by either player.
        self.e = self.o ^ self.mask

    def copy(self):
        '''Returns a copy of the current board.'''
        return Board(b1=self.b1, b2=self.b2, turns=self.turns)

    def moves(self, p1=[], p2=[]):
        '''
        Makes a series of moves for player1 and player2.
        Moves in each list can be either tuples of (row, col) or indices from 0 - 225.

        Parameters
        ----------
        p1 : list of moves to make for player 1.
        p2 : list of moves to make for player 2.

        '''
        tmp = self.turns
        self.turns = 0
        for move in p1:
            # convert row tuple to index
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.force_index(move)

        for move in p2:
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.force_index(move, current=False)
        self.turns = tmp

    def get_board(self, current=True):
        '''
        Returns board of current player if current is set to True.
        Otherwise, returns the board of the other player.
        '''
        if self.turns % 2 == 0 ^ current:
            return self.b2
        return self.b1

    #####################
    # FORCE MOVE
    #####################
    def force_index(self, index, current=True):
        '''
        Forces a move to a certain index in the bitboard.
        Does NOT check if the index is occupied or not, so an illegal move can be made.
        Updates the empty/occupied bitboards.

        Parameters
        ----------
        index: index of the move to make.
        current: whether to make the move for the current player or not.
        '''

        if self.turns % 2 == 0 ^ current:
            self.b2 = gmpy2.bit_set(self.b2, index)
        else:
            self.b1 = gmpy2.bit_set(self.b1, index)

        self.o = gmpy2.bit_set(self.o, index)
        self.e = gmpy2.bit_clear(self.e, index)

    def force_move(self, r, c, current=True):
        self.force_index(r * self.size + c, current=current)

    def force_undo_index(self, index):
        '''
        Clears a move from the bitboard.
        Updates the empty/occupied bitboards.
        '''

        self.b1 = gmpy2.bit_clear(self.b1, index)
        self.b2 = gmpy2.bit_clear(self.b2, index)

        self.e = gmpy2.bit_set(self.e, index)
        self.o = gmpy2.bit_clear(self.o, index)

    #####################
    # VALID
    #####################
    def is_valid_index(self, index):
        '''Determines if the passed in index is a valid move.'''
        return 0 <= index < self.size * self.size and gmpy2.bit_test(self.e, index)

    def is_valid_move(self, r, c):
        return self.is_valid_index(r * self.size + c)

    #####################
    # MOVE
    #####################
    def move_index(self, index):
        '''
        Checks to see if a move is valid. If the move is valid, make it, then increment turns.
        '''
        if not self.is_valid_index(index): raise Exception(f'Invalid cell: {index // 15}, {index % 15}')
        self.force_index(index)
        self.turns += 1

    def move(self, r, c):
        self.move_index(r * 15 + c)

    #####################
    # Slow rotate, only used for testing
    #####################
    def rotate(self):
        '''Returns a board with bits rotated clockwise.'''
        b = Board()
        for r in range(15):
            for c in range(15):
                if gmpy2.bit_test(self.b1, r * 15 + c):
                    b.force_index((14 - c) * 15 + r)
                if gmpy2.bit_test(self.b2, r * 15 + c):
                    b.force_index((14 - c) * 15 + r, current=False)
        return b

    #####################
    # BUILTIN
    #####################
    def __repr__(self):
        return f'b1={self.b1}, b2={self.b2}, turns={self.turns}'

    def __str__(self):
        s = []
        s.append('===================================')
        s.append('    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 ')
        s.append('    ______________________________')
        for row in range(self.size):
            r = f'{row:>2} |'
            for col in range(self.size):
                bit_index = row * 15 + col
                if gmpy2.bit_test(self.b1, bit_index): r += 'o '
                elif gmpy2.bit_test(self.b2, bit_index): r += 'x '
                else: r += '- '
            s.append(r)
        s.append(f'b1={self.b1}, b2={self.b2}, turns={self.turns}')
        s.append('===================================')
        return '\n'.join(s)

    def __eq__(self, other):
        return self.b1 == other.b1 and self.b2 == other.b2

    def __hash__(self):
        return hash((self.b1, self.b2))
