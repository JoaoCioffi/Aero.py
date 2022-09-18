import os
import pandas as pd

absPath = os.path.dirname(__file__)
relPath = "dependencies"
filesPath = os.path.join(absPath,relPath)

def loadData(filename='polar-clarky.txt',path=filesPath):
    os.chdir(filesPath)
    data = pd.read_csv(filename)
    return data