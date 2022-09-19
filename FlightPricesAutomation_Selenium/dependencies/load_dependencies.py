import os
from selenium import webdriver

absPath = os.path.dirname(__file__)
relPath = "MS_Edge_Driver"
filesPath = os.path.join(absPath,relPath)

def findDriverExecutable(filename='msedgedriver.exe',path=filesPath):
    os.chdir(filesPath)
    driver = webdriver.Edge() # in web browser (edge), type: edge://version/ --> Make sure you're using the same version of your browser
    os.chdir(absPath)
    return driver