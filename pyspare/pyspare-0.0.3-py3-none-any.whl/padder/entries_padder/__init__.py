from aryth.bound_entries import max_by
from texting import SP, lange, to_lpad, to_pad
from veho.entries import mapper


def entries_padder(text, ansi=False, fill=SP):
    lpad, pad = to_lpad(ansi=ansi, fill=fill), to_pad(ansi=ansi, fill=fill)
    kw, vw = max_by(text, lange if ansi else len)
    return mapper(text, lambda x: lpad(x, kw), lambda tx: pad(tx, vw, tx))
