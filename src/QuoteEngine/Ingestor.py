import os
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str):
        filename, file_extension = os.path.splitext(path)
        if file_extension == ".txt":
            return TXTIngestor.parse(path)
        elif file_extension == ".docx":
            return DOCXIngestor.parse(path)
        elif file_extension == ".pdf":
            return PDFIngestor.parse(path)
        elif file_extension == ".csv":
            return CSVIngestor.parse(path)
        else:
            raise ValueError("Unsupported file extension:", file_extension)
