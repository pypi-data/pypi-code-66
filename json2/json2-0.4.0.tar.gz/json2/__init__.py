from json import *

def load_file(filename):
    with open(filename, "r") as f:
        return loads(f.read())


def dump_file(filename, content):
    with open(filename, "w") as f:
        f.write(dumps(content))
