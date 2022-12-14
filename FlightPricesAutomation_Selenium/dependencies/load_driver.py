import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options

absPath = os.path.dirname(__file__)
relPath = "MS_Edge_Driver"
filesPath = os.path.join(absPath,relPath)

def findDriverExecutable(filename='msedgedriver.exe',path=filesPath):
    os.chdir(filesPath)
    driver = webdriver.Edge() # in web browser (edge), type: edge://version/ --> Make sure you're using the same version of your browser
    driver_options = Options()
    driver_options.add_argument('--headless'),driver_options.add_argument('--log-level=3'),driver_options.add_experimental_option('excludeSwitches',['enable-logging'])
    os.chdir(absPath)
    return driver
