import TextExtractorV2 as te
import MinerV1 as m
path="C:\\Users\\MRX\\Desktop\\Test.pdf"

result = te.loadPages(path,0,13)
#print(result)

result1 = te.extractTextV2(result)

for item in result1:
    print(item)
