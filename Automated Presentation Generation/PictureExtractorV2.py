import fitz

class image:
    def __init__(self):
        self.imageName = []
        self.imagePage = []

    def addImage(self,imageName,imagePage):
        self.imageName.append(imageName)
        self.imagePage.append(imagePage)


    def extractImages(self,path, pageNum):
        pdf = fitz.open(path)
        list = []
        image_list = pdf.getPageImageList(pageNum)

        for image in image_list:
            xref = image[0]
            pix = fitz.Pixmap(pdf, xref)
            if pix.n < 5:
                pix.writePNG(f'{xref}.png')
            else:
                pix1 = fitz.open(fitz.csRGB, pix)
                pix1.writePNG(f'{xref}.png')
                pix1 = None
            pix = None
            self.addImage(xref,pageNum)

    def extractAllImages(self,path,pageStart,pageEnd):
        for index in range(pageStart,pageEnd):
            self.extractImages(path,index)


#test

path = "C:\\Users\\MRX\\Desktop\\Fake reviews Detection Documetation.pdf"

"""
imageObj = image()
imageObj.extractImages(path,0)
print(imageObj.imageName[0])
"""