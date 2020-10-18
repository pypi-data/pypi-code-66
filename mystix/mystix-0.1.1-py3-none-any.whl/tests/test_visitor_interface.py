from unittest import TestCase
from tests.util.print_program import ProgramPrinter
from tests.util.example_ast import example_1


class VisitorInterfaceTests(TestCase):

    def test_print_visitor(self):
        self.assertEqual(
            "(Program "
                "(Body "
                    "(Loader "
                    "(Var 'source') "
                    "(Source "
                        "'www.coviddata.com/stream')) "
                    "(Mapper "
                        "(Var 'source') "
                        "'case_date' "
                        "(Declare (Type Types.NUMBER) (Var 'date'))) "
                    "(Assigner "
                        "(Declare (Type Types.NUMBER) (Var 'count')) "
                        "(Value 0)) "
                    "(Trigger (Var 'source') ((Increment (Var 'count')))) "
                    "(Plotter (Graph 'scatter') (VarAxis (Var 'date')) "
                        "(VarAxis (Var 'age')) 'age_graph') "
                    "(Plotter (Graph 'line') (VarAxis (Var 'date')) "
                        "(FuncAxis (BuiltinFunc NumFunction.LOG (Var 'count'))) "
            "'age_graph')))",
            ProgramPrinter().print(example_1()))
