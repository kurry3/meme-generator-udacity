import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path) as f:
            for line in f:
                one_line = line.strip('\n').split(' - ')
                new_quote = QuoteModel(one_line[0], one_line[1])
                quotes.append(new_quote)
        print(quotes)
        return quotes


