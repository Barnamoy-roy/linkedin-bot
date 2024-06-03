import sys

from utilities import * 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from termcolor import colored


# initialize driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def main():

    username_str = str(get_username(sys.argv))
    password_str = str(get_password(sys.argv))  

    if "--help" in sys.argv: 
        print(colored("  --n <number> : Number of requests to send", "green"))
        print(colored("  --company <company_name> : Company name to search for", "yellow"))
        print(colored("  --role <role_name> : Role name to search for", "red"))

        driver.quit()
        return 

    # open linkedin login page 
    driver.get("https://www.linkedin.com/login")\

    # fill username 
    username = driver.find_element(By.ID, "username")
    username.send_keys(username_str)

    # enter password 
    password = driver.find_element(By.ID, "password")
    password.send_keys(password_str)

    login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    login_button.click()

    wait(5)

    if is_captcha_present(driver):
        print(colored("Captcha detected. Please solve the captcha.", "red"))
        wait(60) 

    # get company name
    company = get_company(sys.argv)

    # get role name
    role = get_role(sys.argv)

    getPeople(role, company, "Greetings, I recently came across your profile. I feel I could learn a lot from you about this industry.")

def getPeople(role, company, message, max_request=10):

    base_url = f"https://www.linkedin.com/search/results/people/?keywords={role}%20at%20{company}&origin=SWITCH_SEARCH_VERTICAL"
    driver.get(base_url)

    wait(2)

    sent_request = 0    

    # get max requests 
    max_request = get_max_request(sys.argv)

    while sent_request < max_request:
        # list of profiles 
        profiles = driver.find_elements(By.XPATH, '//div[contains(@class, "entity-result__actions")]')
        for profile in profiles:
            if sent_request >= max_request:
                break
            try:
                button = profile.find_element(By.XPATH, './/button[contains(@class, "artdeco-button--secondary")]')
                if button.text.strip() == "Connect":
                    button.click()
                    wait(1)

                    try: 

                        add_message_btn = driver.find_element(By.XPATH, '//button[@aria-label="Add a note"]')
                        add_message_btn.click()
                        wait(1)

                        text_area = driver.find_element(By.ID, "custom-message")
                        text_area.send_keys(message)
                        wait(1)

                        send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send invitation"]')
                        send_button.click()
                        wait(1)

                        sent_request += 1 
                        print(f"Connection request sent successfully. Total requests sent: {sent_request}")
                    
                    except: 

                        try:
                            close_button = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]')
                            close_button.click()
                            wait(2)

                            # Retry clicking the Connect button
                            button.click()
                            wait(2)


                        except:
                            # No modal found, continue
                            pass

                        send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send without a note"]')
                        send_button.click()
                        wait(1)

                        sent_request += 1 
                        print(f"Connection request sent successfully. Total requests sent: {sent_request}")
                    


            except Exception as e:
                print(f"Failed to send connection request: {e}")
        
        # Scroll down to load more profiles
        scroll_to_bottom(driver)

        try:
            next_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Next")]')
            next_button.click()
            wait(5)
        except:
            print("No more pages available or unable to find the next button.")
            break

    print("Finished sending connection requests.")


if __name__ == "__main__":
    welcome_msg()
    main()