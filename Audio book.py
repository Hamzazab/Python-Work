from cgitb import text
import pyttsx3
import PyPDF2

book = open('pak-studies-english-10.pdf' ,'rb')
pdfreader = PyPDF2.PdfFileReader(book) 
pages = pdfreader.numPages
#print(pages)
speaker = pyttsx3.init()
page = pdfreader.getPage(3)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
