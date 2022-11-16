import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def element_wait(driver):
    wait = WebDriverWait(driver, 20)
    return wait


def search_iQOO_Neo6(driver):
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iQOO Neo 6 5G (Dark Nova, 8GB RAM, 128GB Storage) | Snapdragon® 870 5G | 80W FlashCharge")

def search_BoxSearchButton(driver):
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()


def AccountList_hovering(driver):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, 'nav-link-accountList')).perform()
    time.sleep(1)


def clickSignIn(driver):
    driver.find_element(By.LINK_TEXT, "Sign in").click()


def clickEmail(driver):
    driver.find_element(By.ID, "ap_email").send_keys("9415167270")


def clickSignInSubmit(driver):
    driver.find_element(By.CLASS_NAME, "a-button-input").click()


def clickPassword(driver):
    driver.find_element(By.ID, "ap_password").send_keys("Password#1211#")


def clickPasswordSubmit(driver):
    driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()  # ==or-- (By.ID, "signInSubmit")


def cart_click(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.in/gp/cart/view.html?ref_=nav_cart']").click()


def cart_Products(driver):
    products = driver.find_elements(By.CSS_SELECTOR, "input[value='Delete']")
    return products


def cart_DeleteProducts(driver):
    product = driver.find_element(By.CSS_SELECTOR, "input[value='Delete']").click()
    return product


def yourAccount(driver):
    driver.find_element(By.XPATH, "//span[normalize-space()='Your Account']").click()


def login_Security(driver):
    driver.find_element(By.XPATH, "//h2[normalize-space()='Login & security']").click()


def home_page(driver):
    driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']").click()


def icon_Mobiles(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Mobiles')]").click()


def onePlus_mobileOption(driver):
    driver.find_element(By.XPATH, "//span[@class='a-size-base a-color-base'][normalize-space()='OnePlus']").click()


def onePlus_MobileSelect(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'OnePlus Nord CE 2 5G (Bahamas Blue, 8GB RAM, 128GB Storage)')]").click()


def onePlus_iqoomobileSelect(driver):
    driver.find_element(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//span[contains(text(),'iQOO Neo 6 5G (Dark Nova, 8GB RAM, 128GB Storage) ')]").click()


def add_to_cart(driver):
    driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()


def close_ProceedPage(driver):
    driver.find_element(By.XPATH, "//a[@id='attach-close_sideSheet-link']").click()


def cart_hovering(driver):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.in/gp/cart/view.html?ref_=nav_cart']")).perform()
    time.sleep(1)


def product_InCart(driver):
    products = driver.find_elements(By.XPATH, "//div[@id='sc-active-cart']//span[@class='a-truncate-cut']")
    return products
