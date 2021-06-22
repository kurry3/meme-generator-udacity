import os
import csv
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)
        print(quotes)
        return quotes


