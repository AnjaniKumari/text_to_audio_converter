Libraries used:
  1.	gtts: Used for converting text to speech.
  2.	playsound: Used for playing the generated audio file.
  3.	PyPDF2: Used for reading text from PDF files (if applicable).
Functions defined:
  1.read_pdf Function:
    •	Takes a file path as input.
    •	Opens the PDF file in binary mode (rb).
    •	Creates a PdfReader object using PyPDF2.
    •	Extracts text from each page using extract_text().
    •	Returns a list of strings, each containing the text from a page.
  
  2.text_to_speech Function:
    •	Takes text and an optional language parameter (default: 'en').
    •	It has logic for handling both a list of text (from PDF) and a single string (direct text).
    •	Creates a gTTS object using the provided text and language.
    •	Prints myobj (potentially for debugging, can be removed).
    •	Saves the audio as "output.mp3".
    •	Plays the generated audio using playsound.
