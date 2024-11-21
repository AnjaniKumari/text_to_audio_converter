# from gtts import gTTS
# from playsound import playsound
# import PyPDF2


# def read_pdf(file_path):
#   """Reads text from a PDF file.

#   Args:
#     file_path: Path to the PDF file.

#   Returns:
#     A list of strings, each representing a page of text.
#   """

#   with open(file_path, 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     num_pages = len(reader.pages)

#     text = []
#     for page_num in range(num_pages):
#       page = reader.pages[page_num]
#       text.append(page.extract_text())

#     return text



# def text_to_speech(text, language='en'):
#     """
#     Converts text to audio.

#     Args:
#         text: The text to be converted.
#         language: The language of the text.
#     """
#     #in case of pdf access the forst element of pdf text
#     myobj = gTTS(text=text[0], lang=language, slow=False)

#     #in case of text
#     myobj = gTTS(text=text, lang=language, slow=False)
#     print("myobj----->",myobj)
#     myobj.save("output.mp3")
#     playsound("output.mp3")





import PyPDF2
from gtts import gTTS
from playsound import playsound

def read_pdf(file_path):
    """Reads text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        list: A list of strings, where each string represents the text from a page in the PDF.

    Raises:
        FileNotFoundError: If the specified PDF file is not found.
    """

    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return [page.extract_text() for page in reader.pages]
    except FileNotFoundError as e:
        print(f"Error: PDF file not found. ({e})")
        raise

def text_to_speech(text, language='en', choose_page=False):
    """Converts text to speech.

    Args:
        text (str or list): The text to be converted. If a list, it's assumed to be PDF page text.
        language (str, optional): The language of the text. Defaults to 'en' (English).
        choose_page (bool, optional): If True, allows the user to choose a page for PDF conversion. Defaults to False.

    Raises:
        ValueError: If `text` is a list and `choose_page` is False.
    """

    if isinstance(text, list):
        if choose_page:
            page_count = len(text)
            while True:
                try:
                    page_choice = int(input(f"Select a page number (1-{page_count}): "))
                    if 1 <= page_choice <= page_count:
                        text = text[page_choice - 1]  # Adjust indexing for user input
                        break
                    else:
                        print("Invalid page number. Please choose between 1 and", page_count)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            raise ValueError("`choose_page` must be True when `text` is a list of page text.")

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")

file_path = r'pdf file path'
text_data = read_pdf(file_path)
text_to_speech(text_data, choose_page=True)

# # Example usage:
# text = "Hello, world! This is a text-to-speech example."
# text_to_speech(text_data)
