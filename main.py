# Constants
CHROME_DRIVER = "C:\\Users\\Kipplouser1\\Desktop\\Reverse Lookup\\chromedriver"
SITE_KEY = "6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2"
SITE_URL = "https://dashboard.easyleadz.com/elogin"

# Standard Libraries
import os
import time
path = os.path.dirname(os.path.abspath(CHROME_DRIVER))

# Local Libraries 
from recaptcha import recaptcha_response


# Third Party Libraries
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
my_email = os.environ.get('USER_EMAIL')
my_password = os.environ.get('USER_PASS')
api_key = os.environ.get('API_KEY')


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
        os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.maximize_window()
driver.get(SITE_URL)
email_input = driver.find_element(by='id', value='emailId')
password_input = driver.find_element(By.ID, "passwrd")
email_input.send_keys(my_email)
password_input.send_keys(my_password)

recaptcha_response(driver)