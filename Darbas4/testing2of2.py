from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


from time import sleep

#############################################
# SETUP   browser, driver, link

link = "http://suninjuly.github.io/registration1.html"
registration1link = "http://suninjuly.github.io/registration1.html"
registration2link = "http://suninjuly.github.io/registration2.html"

geckodriver_path = r"C:\Users\aluba\OneDrive\Desktop\AppsForVU\GeckoDriver3_2\geckodriver-v0.35.0-win32\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

options = Options()
options.binary_location = firefox_binary_path

service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get(link)
wait = WebDriverWait(driver, 10)
################################################

# To complete the task i need to:
# 1 - Fill out the first form
# 2 - submit it
# 4 - Try to submit the second form
# 5 - It will fail and triger an assert

#################################################

# Kad atlikčiau užduotį, man reikia:
# 1 – užpildykite pirmąją formą
# 2 – pateikti ją (pereis assert, kad viskas pavyko)
# 4 – bandyti pateikti antrą formą
# 5 – tai nepavyks ir trigerins assert'ą

def fill_form(link:str, person:dict):
    try:
        driver.get(link)
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


assert fill_form(registration1link, Person) == True, "Failed to fill 1-st form"
sleep(1)
assert fill_form(registration2link, Person) == True, "Failed to fill 2-nd form"

# Quit driver
driver.quit()
