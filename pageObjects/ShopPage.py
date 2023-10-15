from selenium.webdriver.common.by import By


class ShopPage:
    lnkshop_xpath = "//a[@href='/angularpractice/shop']"
    cardTitle_css = ".card-title a"
    cardFooter_css = ".card-footer button"
    checkout_xpath = "//a[@class='nav-link btn btn-primary']"
    btnquantity_xpath = "(//input[@type='number'])"  # 4
    btnremove_xpath = "//button[@class='btn btn-danger']"  # 4
    finalcheckout_xpath = "//button[@class='btn btn-success']"
    continueshopping_xpath = "//button[@class='btn btn-default']"
    countrybox_xpath = "//*[@id='country']"
    btncheckbox_xpath = "//div[@class='checkbox checkbox-primary']"
    btnpurchase_xpath = "//input[@class='btn btn-success btn-lg']"
    orderconfirmation_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver

    def clickShop(self):
        self.driver.find_element(By.XPATH, self.lnkshop_xpath).click()

    def getCardTitles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cardTitle_css)

    def getCardFooter(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cardFooter_css)

    def checkout(self):
        self.driver.find_element(By.XPATH, self.checkout_xpath).click()

    def increasequantity(self):
        self.driver.find_element(By.XPATH, self.btnquantity_xpath).click()

    def removeitem(self):
        self.driver.find_element(By.XPATH, self.btnremove_xpath).click()

    def finalcheckout(self):
        self.driver.find_element(By.XPATH, self.finalcheckout_xpath).click()

    def continueshopping(self):
        self.driver.find_element(By.XPATH, self.continueshopping_xpath).click()

    def selectplace(self, place):
        self.driver.find_element(By.XPATH, self.countrybox_xpath).send_keys(place)

    def clickcheckbox(self):
        self.driver.find_element(By.XPATH, self.btncheckbox_xpath).click()

    def purchase(self):
        self.driver.find_element(By.XPATH, self.btnpurchase_xpath).click()

    def orderconfirmation(self):
        self.driver.find_element(By.XPATH, self.orderconfirmation_xpath)
