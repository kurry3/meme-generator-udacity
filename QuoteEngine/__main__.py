from QuoteEngine import Ingestor
import os

file_names = ['src\_data\DogQuotes\DogQuotesTXT.txt', 'src\_data\DogQuotes\DogQuotesPDF.pdf',
               'src\_data\DogQuotes\DogQuotesCSV.csv', 'src\_data\DogQuotes\DogQuotesDOCX.docx',
               'src\_data\DogQuotes\DogQuotesIDK.idk']
quote_files = []
project_root = os.path.dirname(os.path.dirname(__file__))
for i in file_names:
    quote_files.append(os.path.join(project_root, i))
print(quote_files)
for f in quote_files:
    try:
        Ingestor.parse(f)
    except ValueError as error:
        print(f"ValueError: {error}")
