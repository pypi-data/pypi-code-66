from typing import Optional, cast


from mystix.language.shared import ast
from mystix.language.tokenization import Tokenizer
from mystix.language.shared.primitives import Types
from mystix.language.shared.primitives import values, graphs
from mystix.language.shared.primitives.numerical import NumOp, NumFunction


class ParseError(Exception):
    pass


class Parser:

    operators = {
        '+=': NumOp.PLUS,
        '-=': NumOp.MINUS,
        '*=': NumOp.TIMES,
        '/=': NumOp.DIV,
        '^=': NumOp.EXP
    }
    bltn = {
        'log': NumFunction.LOG,
        'sin': NumFunction.SIN,
        'cos': NumFunction.COS,
        'exp': NumFunction.EXP
    }

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def parseProgram(self) -> ast.Program:
        commands = []
        self.tokenizer.get_and_check_next("program:")
        self.tokenizer.get_and_check_next(";")
        while(self.tokenizer.more_tokens() and self.tokenizer.check_next() != "start!"):
            command = self.parseCommand()
            commands.append(command)
        self.tokenizer.get_and_check_next("start!")
        return ast.Program(ast.Body(commands))
    
    def parseCommand(self) -> ast.Command:
        next_token = self.tokenizer.check_next()
        command: Optional[ast.Command] = None
        if (next_token == "map"):
            #print("Parsing Map")
            command = self.parseMapper()
        elif (next_token == "observe"):
            #print("Parsing Trigger")
            command = self.parseTrigger()
        elif (next_token == "plot"):
            #print("Parsing Plotter")
            command = self.parsePlotter()
        # Line is either Loader or Assigner
        line = self.tokenizer.get_line()
        if ("remote" in line):
            #print('Parsing Loader')
            command = self.parseLoader()
        elif ("=" in line and "remote" not in line):
            #print('Parsing Assigner')
            command = self.parseAssigner()
        while (self.tokenizer.check_next() in ['\n', ';']):
            self.tokenizer.get_next()
        if command is not None:
            return command
        else:
            raise ParseError("Could not determine command")
    
    def parseLoader(self) -> ast.Loader:
        var = self.parseVar()
        self.tokenizer.get_and_check_next("=")
        source = self.parseSource()
        return ast.Loader(var, source)

    def parseMapper(self) -> ast.Mapper:
        self.tokenizer.get_and_check_next("map")
        self.tokenizer.get_and_check_next("\(")
        var = ast.Var(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("\)")
        map_from = self.parseString()
        self.tokenizer.get_and_check_next("to")
        declare = self.parseDeclare()
        return ast.Mapper(var, map_from, declare)
    
    def parseDeclare(self) -> ast.Declare:
        var_type = self.parseType()
        var = self.parseVar()
        return ast.Declare(var_type, var)

    def parseAssigner(self) -> ast.Assigner:
        declare = self.parseDeclare()
        self.tokenizer.get_and_check_next("=")
        value = self.parseValue()
        return ast.Assigner(declare, value)

    def parseTrigger(self) -> ast.Trigger:
        self.tokenizer.get_and_check_next("observe")
        self.tokenizer.get_and_check_next("\(")
        var = self.parseVar()
        self.tokenizer.get_and_check_next("\)")
        self.tokenizer.get_and_check_next("do")
        math_funcs = self.parseMathFuncs()
        return ast.Trigger(var, math_funcs)

    def parsePlotter(self) -> ast.Plotter:
        self.tokenizer.get_and_check_next("plot")
        graph = self.parseGraph()
        self.tokenizer.get_and_check_next("\(")
        x_axis = self.parseAxis(',')
        #print("X AXIS GOTTEN")
        self.tokenizer.get_and_check_next(',')
        #print("COMMA CONFIRMED")
        y_axis = self.parseAxis(')')
        self.tokenizer.get_and_check_next("\)")
        self.tokenizer.get_and_check_next("titled")
        name = self.parseString()
        return ast.Plotter(graph, x_axis, y_axis, name)

    def parseSource(self) -> ast.Source:
        self.tokenizer.get_and_check_next("remote")
        self.tokenizer.get_and_check_next("\(")
        self.tokenizer.get_and_check_next("\"")
        url = self.tokenizer.get_next()
        self.tokenizer.get_and_check_next("\"")
        self.tokenizer.get_and_check_next("\)")
        return ast.Source(url)

    def parseMathFuncs(self) -> ast.MathFuncs:
        functions = []
        line = self.tokenizer.get_line(',')
        #print(line)
        functions.append(self.parseFunc(line))
        next_token = self.tokenizer.get_next()
        while(next_token not in ['\n', ';'] and next_token == ','):
            line = self.tokenizer.get_line(',')
            functions.append(self.parseFunc(line))
            next_token = self.tokenizer.get_next()
        return ast.MathFuncs(functions)
    
    def parseAxis(self, endline = ',') -> ast.Axis:
        line = self.tokenizer.get_line(endline)
        #print(line)
        if(len(line) == 1):
            return ast.VarAxis(ast.Var(self.tokenizer.get_next()))
        elif self.isMathFunc(line):
            func = self.parseFunc(line)
            return ast.FuncAxis(func)
        else:
            raise ParseError("Could not parse axis")

    def parseFunc(self, line) -> ast.Func:
        func: Optional[ast.Func] = None
        if (self.isFastFunc(line)):
            func = self.parseFastFunc()
        elif (self.isSimpFunc(line)):
            func = self.parseSimpFunc()
        elif (self.isBltnFunc(line)):
            func = self.parseBltnFunc()
        #print(func)
        #print(self.tokenizer.check_next())
        if func is not None:
            return func
        else:
            raise ParseError("Could not determine function")

    def parseSimpFunc(self) -> ast.SimpleFunc:
        var = ast.Var(self.tokenizer.get_next())
        op = self.tokenizer.get_next()
        op += self.tokenizer.get_next()
        concrete_op: NumOp = self.operators[op]
        value = self.parseValue()
        return ast.SimpleFunc(var, ast.Operand(concrete_op), value)
    
    def parseFastFunc(self) -> ast.FastFunc:
        token = self.tokenizer.get_next()
        var = ast.Var(token[:-2])
        operator = token[-2:]
        if operator == '++':
            return ast.Increment(var)
        else:
            return ast.Decrement(var)
    
    def parseBltnFunc(self) -> ast.BuiltinFunc:
        op = self.tokenizer.get_next()
        f: NumFunction = self.bltn[op]
        self.tokenizer.get_and_check_next("\(")
        var = self.tokenizer.get_next()
        self.tokenizer.get_and_check_next("\)")
        return ast.BuiltinFunc(f, op)

    def parseString(self) -> str:
        self.tokenizer.get_and_check_next('"')
        string_token = ''
        while(self.tokenizer.check_next() != '"'):
            string_token += self.tokenizer.get_next()
        self.tokenizer.get_and_check_next('"')
        return string_token

    def parseGraph(self) -> ast.Graph:
        graph = self.tokenizer.get_next()
        if graph == 'scatter_xy':
            return ast.Graph(graphs.ScatterXYGraph())
        elif graph == 'line_xy':
            return ast.Graph(graphs.LineXYGraph())
        return ast.Graph(graph)

    def parseVar(self) -> ast.Var:
        return ast.Var(self.tokenizer.get_next())

    def parseValue(self) -> ast.Value:
        next_token = self.tokenizer.get_next()
        val = next_token
        # String Case
        if next_token == '"':
            val = ''
            next_token = self.tokenizer.get_next()
            val += next_token
            while (next_token != '"'):
                val += self.tokenizer.get_next()
            return ast.Value(values.CategoricalValue(val))
        # Binary Boolean case
        elif next_token.lower() == 'true':
            return ast.Value(values.BinaryValue(True))
        elif next_token.lower() == 'false':
            return ast.Value(values.BinaryValue(False))
        else:
            try:
                if "." in val:
                    return ast.Value(values.FloatValue(float(val)))
                else:
                    return ast.Value(values.IntegerValue(int(val)))
            except TypeError:
                raise ParseError("Could not parse value '%s'" % val)

    def parseType(self) -> ast.Type:
        t = self.tokenizer.get_next()
        if t == 'number':
            return ast.Type(Types.NUMBER)
        elif t == 'binary':
            return ast.Type(Types.BINARY)
        else:
            return ast.Type(Types.CATEGORY)

    def isSep(self, input: str) -> bool:
        if (input == ';' or input == '\n'):
            return True
        return False

    def isMathFunc(self, line):
        if (self.isSimpFunc(line) or self.isFastFunc(line) or self.isBltnFunc(line)):
            return True
        return False

    def isFastFunc(self, line):
        ops = ['++', '--']
        if (len(line) == 1 and line[0][-2:] in ops):
            return True
        return False

    def isSimpFunc(self, line):
        if (len(line) == 4 and str(line[1] + line[2]) in self.operators):
            return True
        return False

    def isBltnFunc(self, line):
        if (line[0] in self.bltn):
            return True
        return False
