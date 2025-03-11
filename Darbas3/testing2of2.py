from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from time import sleep
from math import log, sin
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#############################################
# SETUP   browser, driver, link

link = "http://suninjuly.github.io/redirect_accept.html"

geckodriver_path = r"C:\Users\aluba\OneDrive\Desktop\AppsForVU\GeckoDriver3_2\geckodriver-v0.35.0-win32\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

options = Options()
options.binary_location = firefox_binary_path

service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get(link)

wait = WebDriverWait(driver, 10)
org_window = driver.current_window_handle
################################################

# To complete the task i need to:
# 1 - Press the "magical journey" button
# 2 - Go to the new opened tab
# 3 - Get the text from label (the math equation)
# 4 - Solve the math equation
# 5 - Send the answer to the input field
# 6 - Press "Submit" button"
# 7 - Extract the "Stepik quiz" code from alert


#################################################
# 1
driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()

#################################################
# 2
driver.find_element(By.XPATH, "/html/body").send_keys(Keys.SHIFT + Keys.TAB)
wait.until(EC.number_of_windows_to_be(2))

#################################################
# 3                                       /html/body/form/div/div/div/label/span[1]
for window_handle in driver.window_handles:
    if window_handle != org_window:
        driver.switch_to.window(window_handle)
        print(f'Switched to {window_handle}')
        break
wait.until(EC.presence_of_element_located((By.ID, "input_value")))
x_value = int(driver.find_element(By.ID, "input_value").text)

#################################################
# 4
# ans = eval(equation.replace("x", x_value))
ans = log(abs(12 * sin(x_value)))
# print(ans)

#################################################
# 5
driver.find_element(By.ID, "answer").send_keys(str(ans))
sleep(0.5)

#################################################
# 6
driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()
wait.until(EC.alert_is_present())

#################################################
# 7
res = driver.switch_to.alert.text
print(res[res.find(":")+2:].strip())



# Quit driver
driver.quit()
