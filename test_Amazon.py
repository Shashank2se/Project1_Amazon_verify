import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import Method_Module

Service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.in/")

logger = logging.getLogger(__name__)
filehandler = logging.FileHandler("Amazon_logfile.log")
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)


def test_signin_verification():
    Method_Module.login(driver, logger)                         #-------sign in procedure---------
    Method_Module.account_verify(driver, logger)                #------- account varification----------


def test_cart_itemdelete():
    Method_Module.cart_itemdelete(driver, logger)                #------- add to cart check and delete previous items----------


def test_mobile_purchase():
    Method_Module.amazon_Home(driver, logger)                   #----- Amazon home page-----
    Method_Module.mobile(driver, logger)                        #----- Selection of mobile ------
    Method_Module.cart_productVerification(driver, logger)      #------ Cart Product Verification-----
