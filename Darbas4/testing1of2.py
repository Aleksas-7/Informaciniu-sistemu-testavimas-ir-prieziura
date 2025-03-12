from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
from math import log, sin

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#############################################
# SETUP   browser, driver, link

link = "http://suninjuly.github.io/explicit_wait2.html"

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
# 1 - Press the "book" button on 100$ price
# 2 - Get the text from label (the math equation)
# 3 - Solve the math equation
# 4 - Send the answer to the input field
# 5 - Press "Submit" button"
# 6 - Extract the "Stepik quiz" code from alert

#################################################
# 1
wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
driver.find_element(By.ID, "book").click()



#################################################
# 2
wait.until(EC.presence_of_element_located((By.ID, "input_value")))
driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
x_value = driver.find_element(By.ID, "input_value").text

#################################################
# 3
ans = log(abs(12 * sin(int(x_value))))

#################################################
# 4
driver.find_element(By.ID, "answer").send_keys(str(ans))
sleep(0.5)

#################################################
# 5
driver.find_element(By.ID, "solve").click()
wait.until(EC.alert_is_present())

#################################################
# 7
res = driver.switch_to.alert.text
print(res[res.find(":")+2:].strip())


sleep(1)
# Quit driver
driver.quit()
