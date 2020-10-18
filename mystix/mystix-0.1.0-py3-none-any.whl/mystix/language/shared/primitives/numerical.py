from enum import Enum


class NumFunction(Enum):
    LOG = "log"
    SIN = "sin"
    COS = "cos"
    EXP = "exp"


class NumOp(Enum):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIV = "/"
    EXP = "^"
