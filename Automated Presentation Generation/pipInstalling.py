import sys
import subprocess

# implement pip as a subprocess:
def installPackages(listOfPackages):

    for item in listOfPackages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',item])

listOfPackages = ["PySimpleGUI","PyPDF2", "spaCy","heapq_max", "Pymupdf","Fitz", "pdfminer.six", "Python-pptx" ,"pdfminer"]
