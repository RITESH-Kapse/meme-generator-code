from QuoteEngine import DocxImporter,CSVImporter

# print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

# print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))

from QuoteEngine import Ingestor , PDFImporter

print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))

#print(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))