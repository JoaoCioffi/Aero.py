 # ---// UNDER DEVELOPMENT //--- #

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Filters:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def applyAirlinesFilter(self):
        availableAirlinesDiv = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="resultPage-AIRLINESFilter-content"'
        )
        
        for items in availableAirlinesDiv:
            airlines = self.driver.find_element(
                By.CSS_SELECTOR,
                'li[class="css-swohae epwz15m3"'
            )
            print(airlines.text)
           
