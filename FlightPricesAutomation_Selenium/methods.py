from dependencies import constants as const,\
                         load_driver as ld
from selenium.webdriver.common.by import By

class Booking():

    def __init__(self,driver=ld.findDriverExecutable(),teardown=False):
        self.driver = driver
        self.driver.teardown = teardown #close application (browser) after execution
        super(Booking, self).__init__()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
    
    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def acceptCookies(self):
        try:
            acceptElement = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="cookieBanner-confirmButton"]')
            print('\nThis website uses cookies.\n')
            acceptElement.click()
        except:
            print('\nNo cookies elements were found. Skipping...\n')
    
    def selectDeparture(self,departureLocation):
        search_field = self.driver.find_element(By.ID,'searchForm-singleBound-origin-input')
        search_field.clear() #clears text if already filled

        print('\n>> Sending Keys...')
        search_field.send_keys(departureLocation)
        print(f'\n * Selected Departure Location : {departureLocation} ✈︎\n')

        first_result = self.driver.find_element(By.ID,'react-select-2-option-0')
        first_result.click()
    
    def selectArrival(self,arrivalLocation):
        search_field = self.driver.find_element(By.ID,'searchForm-singleBound-destination-input')
        search_field.clear() #clears text if already filled

        print('\n>> Sending Keys...')
        search_field.send_keys(arrivalLocation)
        print(f'\n * Selected Arrival Location : {arrivalLocation} ✈︎\n')

        first_result = self.driver.find_element(By.ID,'react-select-3-option-0')
        first_result.click()

    def __exit__(self):
        if self.driver.teardown:
            self.driver.quit()