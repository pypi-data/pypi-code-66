from mystix.ui.util import read_program_file
from mystix.language.tokenization import Tokenizer, TokenizationError
from mystix.language.parsing import Parser, ParseError
from mystix.language.evaluation import Evaluator


def process(content: str, e: Evaluator):
    try:
        t = Tokenizer(content)
        t.tokenize()
        p = Parser(t).parseProgram()
        return e.evaluate(p, duration=5000)
    except (TokenizationError, ParseError) as e:
        print("\nERROR: %s\n" % str(e))
        return 2, e


def run_program(filename: str, graphics=False):
    try:
        return read_program_file(filename, lambda c: process(c, Evaluator(
            graphics=graphics)))
    except FileNotFoundError as e:
        print("\nERROR: Could not read file '%s'\n" % filename)
        return 3, e
