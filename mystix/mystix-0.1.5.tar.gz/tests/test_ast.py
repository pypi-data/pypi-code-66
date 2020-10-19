import unittest

from mystix.language.shared import ast, primitives


class ASTTests(unittest.TestCase):

    def test_program_construction(self):
        try:
            v: ast.Var = ast.Var("placeholder")
            t: ast.Type = ast.Type(primitives.Types.NUMBER)
            d: ast.Declare = ast.Declare(t,v)
            b: ast.Body = ast.Body([ast.commands_ast.Assigner(d,4), ast.commands_ast.Assigner(d,"hello")])
            p: ast.Program = ast.Program(b)
        except TypeError:
            self.fail("Failed to build")
