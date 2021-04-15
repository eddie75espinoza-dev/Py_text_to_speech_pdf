import os
import PyPDF2 # lector de pdf
import pyttsx3 # speak

CURR_DIR = os.path.dirname(os.path.realpath(__file__)) # tambien se puede usar = CURR_DIR = os.getcwd()
speak = pyttsx3.init() # object creation

def get_text(page_pdf):
    if validate_page:
        from_page = pdf_reader().getPage(page_pdf) #get details from pdf's page
        text = from_page.extractText()    
    return text

def pdf_reader():
    pdfReader = PyPDF2.PdfFileReader(path)    
    return pdfReader


def validate_page(page_init, page_end):
    pages_pdf = pdf_reader().numPages
    if page_init > pages_pdf:
        print(f'Page not found, verify page initial')
        return False
    elif page_end > pages_pdf:
        print(f'Page not found, end page = {pages_pdf}')
        return False
    return True

def play_voice(text_languaje):  
    ''' Changing Voices '''  
    voices = speak.getProperty('voices')
    
    if text_languaje == 0:
        return speak.setProperty('voice', voices[0].id) #changing index, changes voices. 0 for female in Spanish
    if text_languaje == 1:
        return speak.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female in English
    if text_languaje == 2:
        return speak.setProperty('voice', voices[2].id) #changing index, changes voices. 2 for male in English

def playPdf(page_init, page_end, text_languaje):
    page_init -=1
    speak = pyttsx3.init()    
    play_voice(text_languaje)    
    if validate_page(page_init, page_end):
        i = page_init
        for i in range(i, page_end):              
            speak.say(get_text(i))             
            speak.runAndWait()
            speak.stop()

if __name__ == '__main__':
    name_file = input('Enter the name of the .pdf file: ').strip()
    path = open(CURR_DIR + '/' + name_file, 'rb')
    text_languaje = int(input('''Indicates the file language:
~ 0- Spanish / Female 
~ 1- English / Female
~ 2- English / Male: '''))    
    page_init, page_end= input('Initial page and end page: ').strip().split()
    #page_end = input('End page: ').strip()
    playPdf(int(page_init), int(page_end), text_languaje)

    
