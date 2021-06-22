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

        quotes = []
        tmp = f'tmp\{random.randint(0, 1000)}.txt'
        project_root = os.path.dirname(os.path.dirname(__file__))
        tmp = os.path.join(project_root, tmp)
        print(tmp)
        call = subprocess.call(['pdftotext', path, tmp])
        quotes = TXTIngestor.parse(tmp)
        os.remove(tmp)
        return quotes


