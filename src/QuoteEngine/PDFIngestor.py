import os
import subprocess
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        try:
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'

            print(tmp)
            call = subprocess.call(['pdftotext', path, tmp])
            quotes = []
            with open(tmp) as f:
                for line in f.readlines():
                    one_line = line.strip('\n').split(' - ')
                    new_quote = QuoteModel(one_line[0], one_line[1])
                    quotes.append(new_quote)
            print(quotes)
            os.remove(tmp)
        except Exception as e:
            raise Exception("pdf parsing issue occurred.")
        return quotes


