import TextExtractorV2 as teV2
import PictureExtractorV2 as pe
import summarization as summ
import PowerPointMaker as pp
import os
import OsHelper
path = "C:\\Users\\MRX\\Desktop\\Test1.pdf"
startPage = 0
endPage = 11

resultList = teV2.loadPages(path, startPage, endPage)

titleAndTextAndPageList = teV2.extractTextV2(resultList)

extractedImage = pe.image()

extractedImage.extractAllImages(path, startPage,endPage)

for i in range(len(titleAndTextAndPageList)):
    print(titleAndTextAndPageList[i])
    summarizedText = summ.sumarize(titleAndTextAndPageList[i][1])
    if len(summarizedText) > 1:
        titleAndTextAndPageList[i][1] = summarizedText
    print(titleAndTextAndPageList[i])

for item in titleAndTextAndPageList:
    print(item)

pp.makePowerPoint(titleAndTextAndPageList,startPage,["No comment","no"], "test" ,extractedImage)

OsHelper.removePngs(extractedImage.imageName)

os.startfile("test.pptx")