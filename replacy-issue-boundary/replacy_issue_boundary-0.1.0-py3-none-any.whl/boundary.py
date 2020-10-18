from typing import List

from spacy.tokens import Span


class ReplacyPipelineOrderError(RuntimeError):
    pass


class ESpan(Span):
    @staticmethod
    def create_instance(span: Span):
        espan = ESpan(span.doc, span.start, span.end, span.label, span.vector, span.vector_norm, span.kb_id)
        espan.start_character = espan.start_char
        espan.end_character = espan.end_char
        espan.fixed_text = espan.text
        return espan

    def __getattribute__(self, item):
        if item == 'start_char' and hasattr(self, 'start_character'):
            return self.start_character
        elif item == 'end_char' and hasattr(self, 'end_character'):
            return self.end_character
        elif item == 'text' and hasattr(self, 'fixed_text'):
            return self.fixed_text
        else:
            return object.__getattribute__(self, item)

    def update_boundary(self, start, end):
        self.start_character = start
        self.end_character = end
        self.fixed_text = self.doc.text[start:end]


class IssueBoundary:
    def __init__(self, name="IssueBoundary"):
        self.name = name

    @staticmethod
    def would_cause_lowercase_first_letter(span: Span) -> bool:
        return (
                span.start_char == 0
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    @staticmethod
    def would_cause_double_space(span: Span) -> bool:
        return (
                span.start_char > 0
                and span.end_char < len(span.doc.text)
                and len(span._.suggestions) > 0
                and span.doc.text[span.start_char - 1] == " "
                and span.doc.text[span.end_char] == " "
                and span._.suggestions[0] in ["", ","]
        )

    @staticmethod
    def would_cause_space_at_start(span: Span) -> bool:
        return (
                span.start_char == 0
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    def __call__(self, spans: List[Span]) -> List[Span]:
        result = []
        for span in spans:
            start, end = span.start_char, span.end_char
            if IssueBoundary.would_cause_space_at_start(span):
                # space at start, extending issue forward one character
                end += 1
            if IssueBoundary.would_cause_lowercase_first_letter(span):
                # casing issue, extending issue forward one word and uppercasing that word
                doc_text_without_issue = span.doc.text[end:]
                first_space_index = doc_text_without_issue.find(' ')
                replacement = doc_text_without_issue[0:first_space_index]
                end += first_space_index
                span._.suggestions = [replacement.title()]
            if IssueBoundary.would_cause_double_space(span):
                # double space issue, extending issue back one character
                start -= 1
            espan = ESpan.create_instance(span)
            espan.update_boundary(start, end)
            result.append(espan)
        return sorted(result, key=lambda span: span.start)
