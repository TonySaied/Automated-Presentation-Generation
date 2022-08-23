from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LTLine,LAParams
import os
path="C:\\Users\\MRX\\Desktop\\Fake reviews Detection Documetation.pdf"

import fitz

fontSizes=[]
uniqueFontSizes = {}
def scrape( filePath):
    results = [] # list of tuples that store the information as (text, font size, font name)

    pdf = fitz.open(filePath) # filePath is a string that contains the path to the pdf
    i = 0
    for page in pdf:
        dict = page.get_text("dict")
        blocks = dict["blocks"]
        for block in blocks:
            if "lines" in block.keys():
                spans = block['lines']
                for span in spans:
                    data = span['spans']
                    for lines in data:
                        results.append((lines['text'], lines['size'], i))

                        fontSizes.append(lines['size'])

                        if not lines['size'] in uniqueFontSizes or len(uniqueFontSizes) == 0:
                            uniqueFontSizes[lines['size']] = 1
                        else:
                            uniqueFontSizes[lines['size']] += 1
                        # lines['text'] -> string, lines['size'] -> font size, lines['font'] -> font name
        i += 1
    pdf.close()
    return results

def scrapeV2 (filePath,pageStart,pageEnd):
    results = []  # list of tuples that store the information as (text, font size, font name)

    pdf = fitz.open(filePath)  # filePath is a string that contains the path to the pdf
    i = 0
    j = 0
    for page in pdf:
        if i in range(pageStart , pageEnd):
            dict = page.get_text("dict")
            blocks = dict["blocks"]
            pageContent=[]
            for block in blocks:
                if "lines" in block.keys():
                    spans = block['lines']
                    for span in spans:
                        data = span['spans']
                        for lines in data:
                            pageContent.append((lines['text'], lines['size'],j))

            results.append(pageContent)
                        # lines['text'] -> string, lines['size'] -> font size, lines['font'] -> font name
        j += 1
    pdf.close()
    return results

#result=scrapeV2(path)
#print(result[69])
#print(fontSizes)

#print(uniqueFontSizes)

def getCommonFontSize(fontsDict):
    max = -999999
    fontSize = 0
    for key in fontsDict.keys():
        if fontsDict[key]>max:
            max = fontsDict[key]
            fontSize = key
    return fontSize

def getCommonTuples(resultList,numOfPages):
    dict = {}
    for tuple1 in  resultList:
        if not tuple1 in dict or len(dict)==0:
            dict [tuple1] = 1
        else:
            dict[tuple1] += 1
    newListOfTuples = []
    for tuple1 in dict.keys():
        if dict[tuple1] >= numOfPages - 2:
            newListOfTuples.append(tuple1)
    return newListOfTuples

def removePagesFooter(resultList):
    for tuple in resultList:
        if tuple[0].lower().__contains__("page"):
            resultList.remove(tuple)
    return resultList

def removeCommonTuples(resultList,commonList):
    for item in commonList:
        if item in resultList:
            resultList.remove(item)
    return resultList

def removeWhiteSpaces(resultList):
    for tuple1 in resultList:
        if tuple1[0] == ' ' or tuple1[0] == '':
            resultList.remove(tuple1)
    return resultList
