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
            acceptElement = self.driver.find_element(
                By.CSS_SELECTOR,
                'button[data-testid="cookieBanner-confirmButton"]'
                )
            print('\n>> This website uses cookies!\n')
            acceptElement.click()
        except:
            print('\n>> No cookies elements were found. Skipping...\n')
    
    def selectDeparture(self,departureLocation):
        searchField = self.driver.find_element(
            By.ID,
            'searchForm-singleBound-origin-input'
            )
        searchField.clear() #clears text if already filled

        print('\n>> Sending Keys...')
        searchField.send_keys(departureLocation)
        print(f'\n * Selected Departure Location : {departureLocation} 🡽\n')

        depLocationFirstResult = self.driver.find_element(
            By.ID,
            'react-select-2-option-0'
            )
        depLocationFirstResult.click()

    
    def selectArrival(self,arrivalLocation):
        searchField = self.driver.find_element(
            By.ID,
            'searchForm-singleBound-destination-input'
            )
        searchField.clear() #clears text if already filled

        print('\n>> Sending Keys...')
        searchField.send_keys(arrivalLocation)
        print(f'\n * Selected Arrival Location : {arrivalLocation} 🢆\n')

        arrFirstResult = self.driver.find_element(
            By.ID,
            'react-select-3-option-0'
            )
        arrFirstResult.click()


    # ---// UNDER DEVELOPMENT //--- #
    """
    def searchCalendar(self,departureDate,arrivalDate):

        # Defining departure parameters:
        departureDateField = self.driver.find_element(
            By.ID,
            'singleBound.departureDate'
            )
        departureDateField.click()
        departureDateElement = self.driver.find_element( #root > div > div.etiMainContent.css-egz5i3.ep8ahwd2 > main > section > div.css-11kfbbt.e9vh9261 > div > div > form > div.css-ieri5n.e1m2ks5t2 > div:nth-child(2) > div > div.css-1pg2y69 > div > div > div.DayPicker.css-t96cw0 > div > div.DayPicker-Months > div > div.DayPicker-Body > div:nth-child(4) > div.DayPicker-Day.DayPicker-Day--today
            By.CSS_SELECTOR, 
            f'div[class="Day-Picker-Day"]/div[aria-label="{departureDate}"]' # expected format: 'Tue Sep 20 2022'
        )
        departureDateElement.click()

        # Defining arrival paramenters:
        arrivalDateField = self.driver.find_element(
            By.ID,
            'singleBound.returnDate'
        )
        arrivalDateField.click()
        arrivalDateElement = self.driver.find_element(
            By.CSS_SELECTOR,
            f'div[class="Day-Picker-Day"]/div[aria-label="{arrivalDate}"]' # expected format: 'Tue Sep 20 2022'
        )
        arrivalDateElement.click()
    """ 

    def directFlightsOnly(self,checkbox=False):
        if checkbox == True:
            directFlightCheckBox = self.driver.find_element(
            By.ID,
            'directFlightCheckbox'
            )
            print('\n>> Selected Direct Flights Only!\n')
            directFlightCheckBox.click()

    def searchFlights(self):
        searchButton = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="searchForm-searchFlights-button"]'

        )
        print('\n>> Searching results...\n')
        searchButton.click()

    def toggleFilters(self,filters=False):
        if filters == True:
            filtersButton = self.driver.find_element(
                By.CSS_SELECTOR,
                'button[data-testid="resultPage-toggleFiltersButton-button"'
            )
            filtersButton.click()

    def __exit__(self):
        if self.driver.teardown:
            self.driver.quit()