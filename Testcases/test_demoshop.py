import time
import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_shop:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_shop(self):
        self.logger.info("   Test_001_Shop")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.sp = ShopPage(self.driver)
        self.logger.info("   Visiting Shop Site")
        self.sp.clickShop()
        self.logger.info("   Adding items to cart")
        cards = self.sp.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                self.sp.getCardFooter()[i].click()

        self.logger.info("   Checkout Page")
        self.sp.checkout()
        self.logger.info("   Final Checkout")
        self.sp.finalcheckout()
        self.logger.info("   Verifying Address")
        self.sp.selectplace("India")
        time.sleep(5)
        self.place = self.driver.find_element(By.XPATH, "//a[normalize-space()='India']")
        self.place.click()
        self.sp.clickcheckbox()
        self.sp.purchase()
        self.logger.info("   Completed the Purchasing Process")
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        if 'Success! Thank you! Your order will be delivered in next few weeks :-).' in textMatch:
            assert True
            self.logger.info("   Successfully Completed Shopping")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_demoshop_scr.png")
            self.logger.error("   Shopping Unsuccessful")
            assert False
