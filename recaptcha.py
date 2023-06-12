SITE_URL = "https://dashboard.easyleadz.com/elogin"
SITE_KEY = "6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2"
REQUEST_URL = "http://2captcha.com/in.php"
RESPONSE_URL = "http://2captcha.com/res.php"


import os
import sys
import time

import requests
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
MY_API_KEY = os.environ.get('API_KEY')


"""Captcha Resolver for v2"""
def captcharesolver():
    solver = TwoCaptcha(MY_API_KEY)

    try:
        result = solver.solve_captcha(
            site_key=SITE_KEY,
            page_url=SITE_URL)
    except Exception as e:
        sys.exit(e)
    else:
        response_site = requests.get(SITE_URL)
        
        # Requesting RECAPTCHA ID 
        response = requests.get(REQUEST_URL, params= {
                                 "key": os.environ.get("API_KEY"), 
                                 "method": "userrecaptcha", 
                                 "googlekey": SITE_KEY, 
                                 "pageurl": SITE_URL
                                })
        
        # Getting the token
        token_from_captcha = response.text.split("|")[1]
        time.sleep(15)

        # Get the Captcha solver 
        while True:
            time.sleep(10)
            full_request_solution = requests.get(RESPONSE_URL, params={
                'key': MY_API_KEY, 
                'action': 'get', 
                'id':token_from_captcha
                })
            
            if full_request_solution.text[0:2] == 'OK':
                break
        captcha_results = full_request_solution.text[3:]
        
        final_req = full_request_solution.text
        final_request_solution = final_req.split("|")[1]
        print(final_request_solution)
        