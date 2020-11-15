import os

def read(inputFile, outputFile):
    
    if os.path.exists(outputFile):
        os.remove(outputFile) 
    o = open(outputFile, "a")

    with open(inputFile, "rb") as i:
        while (byte := i.read(1)):
            mapped = map(ord, byte)
            o.write(str(mapped))

read('triangle.shp', 'test.txt')