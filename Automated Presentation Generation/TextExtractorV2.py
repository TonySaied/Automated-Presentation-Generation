import MinerV1 as m
import PyPDF2

def loadPages(path,startPage,endPage):
    if endPage > getPageCount(path):
        endPage = getPageCount(path)
    pagesScraped = m.scrape(path)
    pageCount = getPageCount(path)
    pagesCommonTuples=m.getCommonTuples(pagesScraped,pageCount)



    extractedPages = m.scrapeV2(path , startPage , endPage)

    for index in range(len(extractedPages)):
        extractedPages[index] = m.removeCommonTuples(extractedPages[index],pagesCommonTuples)
        extractedPages[index] = m.removePagesFooter(extractedPages[index])
        extractedPages[index] = m.removeWhiteSpaces(extractedPages[index])
    result = []
    for item in extractedPages:
        result += item
    return result

def getPageCount(path):
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageCount = int(pdfReader.getNumPages())
    return pageCount
#i = 0 1 2
#j in range (0+18*i,18+18*i)
#extracted pages list list of tuples
def extractText(extractedPageList):
    commonSize = m.getCommonFontSize(m.uniqueFontSizes)
    textList = []
    for i in range(len(extractedPageList)):
        temp = textClass()
        tempTuple = extractedPageList[i]
        if tempTuple[1] > commonSize:
            temp.page = i
            while (extractedPageList[i][1] == commonSize):
                temp.text += tempTuple[0]
                i += 1
                tempTuple = extractedPageList[i]

        else:
            temp.title = tempTuple[0]
        textList.append(temp)
    return textList

def extractTextV2(extractedPageList):
    commonSize = m.getCommonFontSize(m.uniqueFontSizes)
    result = []
    i = 0
    title = ""
    text = ""
    page = 0
    while(i < len(extractedPageList)):

        if not title == '' and not text == '':
            title = ""
            text = ""
            page = 0

        if(extractedPageList[i][1]>commonSize):
            title = extractedPageList[i][0]
            page = extractedPageList[i][2]
            i += 1

        elif extractedPageList[i][1] == commonSize:
            while extractedPageList[i][1] == commonSize and i <len(extractedPageList):
                text += extractedPageList[i][0]+" "
                i += 1
                if not i < len(extractedPageList):
                    break
            result.append([title.strip(), text.strip(), page])
        else:
            i += 1

    return result
