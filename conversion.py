import os
import concurrent.futures
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, create_pages
from gtts import gTTS
from playsound import playsound

# Open the PDF file
with open('document.pdf', 'rb') as file:
    # Create a PDF resource manager object
    resource_manager = PDFResourceManager()
    
    # Create a string buffer
    buffer = StringIO()
    
    # Create a PDF converter object
    converter = TextConverter(resource_manager, buffer, codec='utf-8', laparams=LAParams())
    
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(resource_manager, converter)
    
    # Extract the pages from the PDF
    pages = create_pages(file)
    
    # Convert the pages in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(interpreter.process_page, page) for page in pages]
        concurrent.futures.wait(futures)
    
    # Close the converter and buffer
    converter.close()
    buffer.close()
    
    # Get the text from the buffer
    text = buffer.getvalue()
    
    # Convert the text to speech
    audio = gTTS(text)
    
    # Save the audio to an MP3 file
    with open('document.mp3', 'wb') as audio_file:
        audio.write_to_fp(audio_file)
    
    # Play the audio file
    playsound('document.mp3')
    
    # Delete the audio file
    os.unlink('document.mp3')
