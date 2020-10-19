

def quote(msg):
    return '\n'.join('> {}'.format(x) for x in msg.split('\n'))

def info(msg):
    return quote(msg)

def warn(msg):
    return quote(msg)

def error(msg):
    return quote(msg)

