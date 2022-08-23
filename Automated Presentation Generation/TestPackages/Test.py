import MinerV1 as m

path="C:\\Users\\MRX\\Desktop\\Test.pdf"

result=m.scrape(path)
#print (m.getCommonFontSize(m.uniqueFontSizes))

#print(m.getCommonTuples(result,70))

print (result)
print(m.getCommonFontSize(m.uniqueFontSizes))
