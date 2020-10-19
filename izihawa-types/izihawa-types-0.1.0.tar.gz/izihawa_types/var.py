def varint(x: int, inverted=False):
    buf = b''
    while True:
        towrite = x & 0x7f
        x >>= 7
        if bool(x) != inverted:
            buf += bytes((towrite | 0x80, ))
        else:
            buf += bytes((towrite, ))
        if not x:
            break
    return buf


def varstr(s: bytes, inverted=False):
    return varint(len(s), inverted=inverted) + s


def process_varint(payload, inverted=False):
    """Read a varint from `stream`"""
    shift = 0
    result = 0
    count = 0
    while True:
        i = payload[count]
        count += 1
        result |= (i & 0x7f) << shift
        shift += 7
        if bool(i & 0x80) == inverted:
            break
    return result, count


def process_varstr(payload, inverted=False):
    n, length = process_varint(payload, inverted=inverted)
    return payload[length:length + n], length + n
