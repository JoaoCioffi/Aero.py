from dependencies import constants as const,\
                         load_dependencies as ld
from selenium.webdriver.common.by import By

class Booking():

    def __init__(self,driver=ld.findDriverExecutable(),killRunningTask=False):
        self.driver = driver
        self.killRunningTask = killRunningTask #close application (browser) after execution
        super(Booking, self).__init__()
    
    def land_first_page(self):
        self.driver.get(const.BASE_URL)
    
    def __exit__(self):
        if self.killRunningTask:
            self.quit()