class QuoteModel:
    author = None
    body = None

    def __init__(self, body, author):
        self.body = body
        self.author = author
