from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

import pytest
from time import sleep

#############################################
# SETUP   browser, driver, links

registration1link = "http://suninjuly.github.io/registration1.html"
registration2link = "http://suninjuly.github.io/registration2.html"

def fill_form(driver, link:str, person:dict):
    try:
        wait = WebDriverWait(driver, 10)
        driver.get(link)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/button")))
        driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys(person["Name"])
        driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys(person["Lastname"])
        driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys(person["Email"])
        driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys(person["Phone"])
        driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input").send_keys(person["Address"])
        
        driver.find_element(By.XPATH, "/html/body/div/form/button").click()

        return True
    
    except NoSuchElementException:
        print("Error: Failed to find element")
        driver.quit()
        return False
    
    except Exception as e:
        print("Error: ", e)
        driver.quit()
        return False


Person = {
    "Name": "Jonas",
    "Lastname": "Jonaitis",
    "Email": "A@B.com",
    "Phone": "+1212121212",
    "Address": "Gera Gatve 1"
}



#############################################
#############################################
#############################################

@pytest.fixture(scope="function")
def driver_(request):
    # A broeser instance for each funciton call

    print(f'\nBrowser driver started!')
    geckodriver_path = r"C:\Users\aluba\OneDrive\Desktop\AppsForVU\GeckoDriver3_2\geckodriver-v0.35.0-win32\geckodriver.exe"
    firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    options = Options()
    options.binary_location = firefox_binary_path

    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    yield driver

    print(f'\nBrowser driver ended!')
    driver.quit()


@pytest.fixture(params=[registration1link, registration2link])
def links_(request):
    return request.param


class TestRegistrationForms:

    def test_registration(self, links_, driver_):
        print(f'!! Testing of {links_} form started\n\n')

        driver = driver_
        assert fill_form(driver, links_, Person) == True, f'Failed to fill {links_} form'

        print(f'!! Testing of {links_} form ended\n\n')






# 4-tos skaidres uzduotys 
#✅ Create test(s) from previous practice ( 2 registration forms ) using pytest
#✅ use fixtures
#✅ use separate browser call for each test
#✅ test should be prepared as class methods

# 5-tos skaidres uzduotys    
#✅ For previous task ( two registration forms ) make fixture, 
# which will open new instance of browser for every test and close it at the end of the test. 
#✅? Pas fixture as parameter to test.
#✅ Try to use yield keyword
#✅(Used function scope) Try to use fixture scopes “function”, “class”, “module”, “session” for scope definition.
#❌ Try to use autouse parameter.

# run test with: pytest -s penktas.py





























# Ismokau shortcut i emoji: windows-key + . arba windows-key + ;