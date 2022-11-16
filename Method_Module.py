import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import Elements_po


def login(driver, logger):
    try:
        logger.info("Sign in procedure start")
        Elements_po.AccountList_hovering(driver)
        Elements_po.clickSignIn(driver)
        Elements_po.clickEmail(driver)
        Elements_po.clickSignInSubmit(driver)
        logger.info("Email ID submit successfully")
        Elements_po.clickPassword(driver)
        Elements_po.clickPasswordSubmit(driver)
        logger.info("Password submit successfully")
        time.sleep(5)

    except Exception as e:
        logger.error("Email ID or Password not matched, resubmission required")
        print("login test fail with error")
        print(e)
        raise


def account_verify(driver, logger):
    try:
        logger.info("Account open successfully")
        wait = Elements_po.element_wait(driver)
        wait.until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))
        Elements_po.AccountList_hovering(driver)
        name = driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").text
        print(name)
        assert "Shashank" in name
        logger.info("Name matched successfully")

    except Exception as e:
        print(e)
        print("Name is incorrect")
        logger.error("Account name not matched, False Account opened")


def cart_itemdelete(driver, logger):
    try:
        Elements_po.cart_click(driver)
        logger.info("Cart opened to delete previously added items")
        products = Elements_po.cart_Products(driver)
        print(len(products))
        for product in products:
            product = Elements_po.cart_DeleteProducts(driver)
            time.sleep(1)
        logger.info("All previous items deleted perfectly")
        to_verify = driver.find_element(By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']").text
        print(to_verify)
        assert "Cart is empty" in to_verify
        logger.info("Cart is empty")
    except Exception as e:
        print(e)
        print("cart test fail")
        logger.error("Not all previous items deleted perfectly, Re-check code")


def amazon_Home(driver, logger):
    Elements_po.home_page(driver)
    logger.info("Home page opened")


def mobile(driver, logger):
    try:
        Elements_po.icon_Mobiles(driver)
        logger.info("Mobile page opened")
        Elements_po.onePlus_mobileOption(driver)
        Elements_po.onePlus_MobileSelect(driver)
        logger.info("OnePlus option selected")
        windowsOpened = driver.window_handles       # -------- page switched------
        driver.switch_to.window(windowsOpened[1])
        logger.info("switched window/page")
        Elements_po.add_to_cart(driver)
        logger.info("OnePlus mobile added to cart")
        Elements_po.close_ProceedPage(driver)
        logger.info("Close proceed/checkout page")
        driver.switch_to.window(windowsOpened[0])
        logger.info("RE-switched initial window")
        Elements_po.search_iQOO_Neo6(driver)
        logger.info("Searched iQOO mobile")
        Elements_po.search_BoxSearchButton(driver)
        Elements_po.onePlus_iqoomobileSelect(driver)
        windowsOpened = driver.window_handles
        driver.switch_to.window(windowsOpened[2])
        logger.info("switched to new iQOO mobile window")
        Elements_po.add_to_cart(driver)
        logger.info("iQOO mobile added to cart")
        Elements_po.close_ProceedPage(driver)
        driver.close()
        logger.info("closed iQOO mobile window")
        driver.switch_to.window(windowsOpened[1])
        driver.close()
        logger.info("closed OnePlus mobile window")
        driver.switch_to.window(windowsOpened[0])
        logger.info("RE-switched initial window")


    except Exception as e:
        print(e)
        print("Mobile Phone not added in cart, recheck code")
        logger.error("Mobile Phone not added in cart, recheck code")


def cart_productVerification(driver, logger):
    try:
        Elements_po.cart_hovering(driver)
        Elements_po.cart_click(driver)
        logger.info("Cart open to check added items")
        products = Elements_po.product_InCart(driver)
        print(len(products))
        iQOO = 0
        OnePlus = 0
        for product in products:
            print(product.text)
            if product.text == "iQOO Neo 6 5G (Dark Nova, 8GB RAM, 128GB Storage) | Snapdragon® 870 5G | 80W FlashCharge":
                iQOO = 1
                logger.info("iQOO mobile successfully added in cart")
            # elif product.text == "OnePlus Nord CE 2 5G (Bahamas Blue, 8GB RAM, 128GB Storage)":
            elif "OnePlus Nord CE 2 5G" in product.text:
                OnePlus = 1
                logger.info("OnePlus mobile successfully added in cart")

        assert iQOO == OnePlus == 1
        print("iQOO neo 6 and OnePlus Nord CE 2 added to cart successfully ")
        logger.info("iQOO and OnePlus mobile successfully added in cart")

    except Exception as e:
        print(e)
        print("cart object not matched with assigned object")
        logger.error("iQOO or OnePlus mobile not added in cart")
