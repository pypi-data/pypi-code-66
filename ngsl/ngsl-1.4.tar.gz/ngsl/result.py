from operator import itemgetter


class Result:
    def __init__(self, ngsl_words, not_ngsl_words) -> None:
        self.ngsl_words = ngsl_words
        self.not_ngsl_words = sorted(not_ngsl_words)

    def __str__(self) -> str:
        return f'{self.ngsl_words}\n{self.not_ngsl_words}'
