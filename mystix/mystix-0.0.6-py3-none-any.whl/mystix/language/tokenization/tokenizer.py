from typing import List
import re


class TokenizationError(Exception):
    pass


class Tokenizer:

    def __init__(self, content: str):
        self.current_token = 0
        self.content = content
        self.fixed_literals = [
            ',', ';', '+=', '-=', '/=', '^=', '*=', 'log', 'sin', 'cos', 'exp',
            'line_xy', 'scatter_xy', 'true', 'false', 'number', 'category',
            'binary', 'remote', 'plot', 'titled', '(', ')', 'do',
            'observe', 'map', 'to', 'program:', 'start!', '=', ' ', '"'
        ]
        self.tokens: List[str] = []
        self.tokenize()

    def tokenize(self) -> List[str]:

        RESERVED_WORD = "$%$"

        tokenized_program = self.content.replace("\n", ";")
        for p in self.fixed_literals:
            tokenized_program = tokenized_program.replace(
                p, RESERVED_WORD + p + RESERVED_WORD)
        tokenized_program = tokenized_program.replace(
            RESERVED_WORD+RESERVED_WORD, RESERVED_WORD)
        if len(tokenized_program) > 0 and tokenized_program.startswith(RESERVED_WORD):
            tokenized_program = tokenized_program[len(RESERVED_WORD):]
        res = tokenized_program.split(RESERVED_WORD)

        # Stretch goal: Optimize with less iterative space/time if possible solution exists
        new_res = []
        for i in res:
            if i.strip():
                new_res.append(i.strip())
        self.tokens = new_res
        return new_res

    def check_next(self):
        if self.current_token < len(self.tokens):
            return self.tokens[self.current_token]
        else:
            return "NO MORE TOKENS"

    def get_next(self):
        if self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
            self.current_token += 1
        else:
            token = "NULLTOKEN"
        return token

    def check_token(self, regexp) -> bool:
        s = self.check_next()
        if re.match(regexp, s) is not None:
            return True
        return False

    def get_and_check_next(self, regexp):
        s = self.get_next()
        if (re.match(regexp, s) == None):
            raise TokenizationError(
                f"Unexpected token! Expected something matching {regexp}, got {s}")
        return s

    def more_tokens(self) -> bool:
        if len(self.tokens) == 0:
            return False
        return self.current_token < len(self.tokens)
        
    def get_line(self, stopper = ';'):
        line = []
        cur_token = self.current_token
        next_token = self.get_next()
        stoppers = [';', stopper]
        while(next_token not in stoppers):
            line.append(next_token)
            next_token = self.get_next()
        self.current_token = cur_token
        return line
