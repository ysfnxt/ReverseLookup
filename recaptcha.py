import os

API_KEY = os.environ.get(API_KEY)
SITE_URL = ""
SITE_KEY = ""


from twocaptcha import TwoCaptcha


result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
  url='https://mysite.com/page/with/recaptcha',
  version='v3',
  param1=...)
  

