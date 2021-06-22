class QuoteModel:
    author = None
    line = None

    def __init__(self, author, line):
        self.line = line
        self.author = author