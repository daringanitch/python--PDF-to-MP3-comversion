import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from gtts import gTTS

def pdf_to_mp3(pdf_file, mp3_file, store_location):
  # Open the PDF file
  with open(pdf_file, 'rb') as file:
    # Create a PDF resource manager object
    rsrcmgr = PDFResourceManager()
    # Set up a StringIO object to hold the PDF text
    text_io = StringIO()
    # Set up a PDF converter object
    converter = TextConverter(rsrcmgr, text_io, laparams=LAParams())
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, converter)
    # Process each page of the PDF
    for page in PDFPage.get_pages(file, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
      interpreter.process_page(page)
    # Get the text from the StringIO object
    text = text_io.getvalue()
    # Generate an MP3 file from the text
    tts = gTTS(text)
    # Save the MP3 file to the specified location
    tts.save(os.path.join(store_location, mp3_file))

# Example usage
pdf_to_mp3('document.pdf', 'audio.mp3', '/path/to/store/location')

