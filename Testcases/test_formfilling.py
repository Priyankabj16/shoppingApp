import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.FormfillingPage import Formfilling
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_Form:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_formfilling(self):
        self.logger.info("  Test_002_Form")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("  Launching Form filling Page")
        self.lp = Formfilling(self.driver)
        self.logger.info("  Filling the details")
        self.lp.setname("Vikram Malhotra")
        self.lp.setemail("vikrammalhotra16@gmail.com")
        self.lp.setpassword("123456789")
        self.lp.clickcheckbox()
        self.lp.clickgender("Male")
        self.lp.ESemployed()
        self.lp.dateofbirth("16-01-1999")
        self.lp.twowaybinding()
        self.lp.clicksubmit()

        self.msg = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text

        print(self.msg)
        if 'Success! The Form has been submitted successfully!.' in self.msg:
            assert True
            self.logger.info("  Successfully filled the form")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_form_scr.png")
            self.logger.error(" Test Unsuccessful")
            assert False
