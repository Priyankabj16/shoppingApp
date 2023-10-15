from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Formfilling:
    name_xpath = "//div/input[@name='name']"
    email_xpath = "//input[@name='email']"
    password_css = "#exampleInputPassword1"
    checkbox_css = "#exampleCheck1"
    drp_gender_css = "#exampleFormControlSelect1"
    employment_status_student_xpath = "//div[@class='form-group']//div[1]"
    employment_status_employed_xpath = "//div[@class='form-group']//div[2]"
    DOB_xpath = "//input[@name='bday']"
    submit_xpath = "//input[@value='Submit']"
    twoway_binding_css = "input[class='ng-untouched ng-pristine ng-valid']"

    def __init__(self, driver):
        self.driver = driver

    def setname(self, name):
        self.driver.find_element(By.XPATH, self.name_xpath).send_keys(name)

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.password_css).send_keys(password)

    def clickcheckbox(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_css).click()

    def clickgender(self, value):
        drp = Select(self.driver.find_element(By.CSS_SELECTOR, self.drp_gender_css))
        drp.select_by_visible_text(value)

    def ESstudent(self):
        self.driver.find_element(By.XPATH, self.employment_status_student_xpath).click()

    def ESemployed(self):
        self.driver.find_element(By.XPATH, self.employment_status_employed_xpath).click()

    def dateofbirth(self, dob):
        self.driver.find_element(By.XPATH, self.DOB_xpath).send_keys(dob)

    def clicksubmit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def twowaybinding(self):
        self.driver.find_element(By.CSS_SELECTOR, self.twoway_binding_css)
