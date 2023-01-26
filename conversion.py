import os
import PyPDF2
from gtts import gTTS

def pdf_to_mp3(pdf_file, mp3_file, store_location):
  # Open the PDF file
  with open(pdf_file, 'rb') as file:
    # Read the PDF contents
    pdf = PyPDF2.PdfFileReader(file)
    # Iterate through each page of the PDF
    for page in range(pdf.getNumPages()):
      # Extract the text from the page
      text = pdf.getPage(page).extractText()
      # Generate an MP3 file from the text
      tts = gTTS(text)
      # Save the MP3 file to the specified location
      tts.save(os.path.join(store_location, mp3_file))

# Example usage
pdf_to_mp3('document.pdf', 'audio.mp3', '/path/to/store/location')
