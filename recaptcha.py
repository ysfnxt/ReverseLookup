SITE_URL = "https://dashboard.easyleadz.com/elogin"
SITE_KEY = "6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2"


import os

from twocaptcha import TwoCaptcha
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method





MY_API_KEY = os.environ.get('API_KEY')
twoCaptcha = TwoCaptcha(MY_API_KEY)
recaptcha_token = twoCaptcha.solve_recaptcha(
    site_url=SITE_URL, 
    site_key=SITE_KEY)

