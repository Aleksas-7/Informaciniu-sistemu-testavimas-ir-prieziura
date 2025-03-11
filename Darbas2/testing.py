from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from time import sleep
from json import loads

def do_tests(inputs:dict, driver)->None:
        
    female_radio = driver.find_element(By.ID, "female")
    male_radio = driver.find_element(By.ID, "male")
    if inputs["gender"] == "Male":
        male_radio.click()
    else:
        female_radio.click()

    fname_input = driver.find_element(By.ID, "inp_fname")
    mname_input = driver.find_element(By.ID, "inp_mname")
    lname_input = driver.find_element(By.ID, "inp_lname")
    fname_input.clear()
    mname_input.clear()
    lname_input.clear()
    fname_input.send_keys(inputs["fname"])
    mname_input.send_keys(inputs["mname"])
    lname_input.send_keys(inputs["lname"])

    birthday_input = driver.find_element(By.ID, "inp_birthday")
    birthday_input.clear()
    birthday_input.send_keys(inputs["birthday_date"])

    personal_code_input = driver.find_element(By.ID, "inp_presCode")
    personal_code_input.clear()
    personal_code_input.send_keys(inputs["personal_code"])

    education_dropdown = driver.find_element(By.ID, "education")
    #education_dropdown.clear()
    education_dropdown.send_keys(inputs["education"])

    phone_input = driver.find_element(By.ID, "phone")
    phone_input.clear()
    phone_input.send_keys(inputs["phone"])

    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys(inputs["email"])

    address_input = driver.find_element(By.ID, "address")
    address_input.clear()
    address_input.send_keys(inputs["address"])

    marital_status_dropdown = driver.find_element(By.ID, "martial_status")
    #marital_status_dropdown.clear()
    marital_status_dropdown.send_keys(inputs["martial_status"])

    professional_pos_dropdown = driver.find_element(By.ID, "professional_pos")
    #professional_pos_dropdown.clear()
    professional_pos_dropdown.send_keys(inputs["professional_pos"])

    work_exp_input = driver.find_element(By.ID, "work_exp")
    work_exp_input.clear()
    work_exp_input.send_keys(inputs["work_exp"])

    field_of_work_dropdown = driver.find_element(By.ID, "field_of_work")
    # field_of_work_dropdown.clear()
    field_of_work_dropdown.send_keys(inputs["field_of_work"])

    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()

    sleep(0.1)

    results_section = driver.find_element(By.ID, "results")
    results_text = results_section.text
    # print(results_text)

    form_res = loads(results_text)
    errors = 0
    for key in form_res.keys():
        if form_res[key] != inputs[key]:
            print(f'!!! {form_res[key]} != {inputs[key]}')
            errors += 1;

    print(f'Test for {inputs["fname"]} is done with {errors} errors')




link = "http://127.0.0.1:5500/index.html"

geckodriver_path = r"C:\Users\aluba\OneDrive\Desktop\AppsForVU\GeckoDriver3_2\geckodriver-v0.35.0-win32\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

options = Options()

options.binary_location = firefox_binary_path

service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get(link)
################################################


form_fields_1 = {
    "gender": "Male",
    "fname": "John", 
    "mname": "",  
    "lname": "Doe", 
    "birthday_date": "1985-03-15", 
    "personal_code": "1234567890",
    "education": "Vocational education", 
    "phone": "+1-555-123-4567", 
    "email": "john.doe@example.com",
    "address": "123 Main St, Anytown, USA",
    "martial_status": "Single",
    "professional_pos": "Working", 
    "work_exp": "5", 
    "field_of_work": "IT"
}

form_fields_2 = {
    "gender": "Female",
    "fname": "Jane",  
    "mname": "Ann", 
    "lname": "Smith",  
    "birthday_date": "1992-11-20",
    "personal_code": "9876543210",
    "education": "Higher college education", 
    "phone": "+44-7700-900-888",  
    "email": "jane.smith@example.co.uk",
    "address": "456 Oak Ave, London, UK",
    "martial_status": "Married",
    "professional_pos": "Studying",
    "work_exp": "8", 
    "field_of_work": "Healthcare"
}

do_tests(form_fields_1, driver)

do_tests(form_fields_2, driver)

# Quit driver
driver.quit()
