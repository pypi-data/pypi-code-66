import fileinput

from cree_sro_syllabics import sro2syllabics

__version__ = "0.1.0"


def sro2syllabics_main():
    for line in fileinput.input():
        print(sro2syllabics(line), end="")
