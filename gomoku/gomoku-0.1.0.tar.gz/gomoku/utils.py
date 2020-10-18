import gmpy2

def to_row(index):
    '''Converts an index to a row.'''
    return (index // 15, index % 15)

def to_index(r, c):
    '''Converts a row, col to an index.'''
    return r * 15 + c

def get_ones(num):
    '''Get indices of ones.'''
    indices = []
    i = 0
    while num:
        one = gmpy2.bit_scan1(num, i)
        if one is None:
            break
        indices.append(one)
        i = one + 1
    return indices
