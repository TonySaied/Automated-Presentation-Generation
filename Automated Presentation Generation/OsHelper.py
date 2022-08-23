import os
def removePngs(list):
    for pic in list:
        os.remove(str(pic)+".png")