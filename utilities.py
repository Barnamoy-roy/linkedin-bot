from termcolor import colored
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 
import os 
import json 

def wait(s): 
    time.sleep(s)

def welcome_msg(): 
    with open("assets/ascii_art.txt", "r") as f:
        print(colored(f.read(), "green"))

def scroll_to_bottom(driver): 
    print(colored("Scrolling to the bottom of the page...", "yellow"))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait(2)

def get_max_request(argv): 
    if "--n" in argv: 
        n_index = argv.index("--n")
        return int(argv[n_index+1])
    else: 
        print(colored("No max request provided, Defaulting to 10", "green"))
        return None

def get_company(argv): 
    if "--company" in argv: 
        company_index = argv.index("--company")
        return argv[company_index+1]
    else: 
        print(colored("No company provided, Defaulting to 'Google'", "green"))
        return "Google"

def get_role(argv): 
    if "--role" in argv: 
        role_index = argv.index("--role")
        return argv[role_index+1]
    else: 
        print(colored("No role provided, Defaulting to 'Software Engineer'", "green"))
        return "Software Engineer"

def is_captcha_present(driver):
    try:
        # Check for the presence of reCAPTCHA iframe
        driver.find_element(By.XPATH, '//iframe[contains(@id, "captcha-internal")]')
        return True
    except NoSuchElementException:
        return False