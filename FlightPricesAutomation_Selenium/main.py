from load_dependencies import findDriverExecutable
from selenium.webdriver.common.by import By

driver = findDriverExecutable()
driver.get("https://www.google.com/")
driver.implicitly_wait(3)
my_element = driver.find_element(By.CLASS_NAME,'gb_d')
my_element.click()