class NonExhaustiveTypeCaseError(Exception):
    def __init__(self):
        super(Exception, self).__init__(
            "Reached end of type cases without a match.")