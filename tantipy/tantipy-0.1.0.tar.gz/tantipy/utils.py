def process_varint(payload):
    """Read a varint from `stream`"""
    shift = 0
    result = 0
    count = 0
    while True:
        i = payload[count]
        count += 1
        result |= (i & 0x7f) << shift
        shift += 7
        if i & 0x80:
            break
    return result, count


# return value, len
def process_varstr(payload):
    n, length = process_varint(payload)
    return payload[length:length + n], length + n
