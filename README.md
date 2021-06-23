
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

Setting Up This Yourself

Import the following libraries:
- Pillow==8.2.0
- Flask==2.0.1
- numpy==1.21.0
- pandas==1.2.5
- requests==2.25.1
- docx==0.2.4

Download and install the pdftotext tool: https://www.xpdfreader.com/download.html

Run the Application
The application can be run with the following command:
- python app.py
The application can be accessed at: https://localhost:5000

Sub-Modules
- QuoteEngine is a class that holds the body and author of a quote
- Ingestor encapsulates the helper classes below, calling the appropriate sub-module's parse function depending on the type of input file
Each of the sub-modules below realize the IngestorInterface which acts as a template for their functions
- CSVIngestor: uses the pandas library to create a list of QuoteModels from a csv file
- PDFIngestor: uses the pdftotext subprocess to create a list of QuoteModels from a pdf file
- DocxIngestor: uses the docx library to create a list of QuoteModels from a docx file
- TextIngestor: uses the built-in python libraries to create a list of QuoteModels from a txt file


