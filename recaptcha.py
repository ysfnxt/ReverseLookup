# Constants
SITE_KEY = '6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2'
SITE_URL = "https://dashboard.easyleadz.com/elogin"
REQUEST_URL = "https://2captcha.com/in.php?"
RESPONSE_URL = "http://2captcha.com/res.php?"

# Standard Libraries
import sys
import os
import time
from time import sleep


# Third Party Libraries 
import requests
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv() 
api_key = os.environ.get('API_KEY')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By



"""Captcha Resolver Function using Selenium and 2captcha API. 
1. Get the API key from 2Captcha API 
2. Find data-sitekey parameter.
3. Submit a HTTP GET request to API URL: http://2captcha.com/in.php 
If everything is fine server will return the ID of your captcha as plain text, 
like: OK|2122988149
4. Make a 15 timeout then submit a HTTP GET request to API URL: 
http://2captcha.com/res.php and get the result.
5. Execute a script to input the result and submit the form
"""

def recaptcha_response(driver):
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey=SITE_KEY,
            url=SITE_URL,
            method = 'userrecaptcha',
            version= 'v2',
            enterprise = 'enterprise',
            action='demo_action',
            score=0.9
        )

    except Exception as e:
        sys.exit(e)

    else:
        id = str(result['code'])
        # Requesting RECAPTCHA ID 
        response = requests.get(REQUEST_URL, params= {
                                 "key": os.environ.get("API_KEY"), 
                                 "method": id, 
                                 "pageurl": SITE_URL
                                })


        captcha_id = str(result['captchaId'])
        
        # Get the Token Captcha 
        result_response = "http://2captcha.com/res.php?key={}&action=get&id={}\
            ".format(api_key,captcha_id)
      


        while True:
            time.sleep(10)
            # Sending a GET request for the captcha result 
            response = requests.get(result_response)

            if response.text[0:2] == 'OK':
                break
        captcha_results = response.text[3:]
        

        # set the value of g-recaptcha-response
        driver.execute_script("""
        document.querySelector('[name="g-recaptcha-response"]').innerText='{}'\
            """.format(captcha_results))
        
        driver.execute_script("""
        document.getElementById('g-recaptcha-response').value='{}'
        """.format(id))

        driver.execute_script("""document.getElementById('myForm').submit()""")

