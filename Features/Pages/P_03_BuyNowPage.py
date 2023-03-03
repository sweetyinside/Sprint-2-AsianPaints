import time

from select import select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BuyNow_Page:

    def __init__(self, driver):
        self.driver = driver

##--------------> Element locator value / elements property  <--------------------

        #self.PincodeElement="//input[@class='pincode']"
        self.PincodeElement="//input[@class='pincode']"
        self.CheckElement="//*[@class='google-map-icon pincode-service-check']"
        self.DropDownElement="//div[@id='productInputQtyBox']"
        self.AddToCart="//*[@class='global-button-white checkout-cart']"
        self.InvalidPin="//span[normalize-space()='Please enter valid pincode']"
        # Element Locators Values

##-----------------------> Method for elements <----------------------------------

    def scroll_page(self):        #---For Scrolling the page
        SCROLLPAGE=self.driver.find_element(By.XPATH, self.PincodeElement)
        self.driver.execute_script("window.scrollBy(0,225)")
        return SCROLLPAGE

    def enter_pincode_textbox(self, pcode):
        enterpin=self.driver.find_element(By.XPATH, self.PincodeElement)
        enterpin.send_keys(pcode)



    def clickaddtocart(self):
        cart=self.driver.find_element(By.XPATH, self.AddToCart)
        cart.click()


    #def ClickOnCheck(self):
    #   CheckButton = self.driver.find_element(By.NAME, self.CheckElement)
    #  CheckButton.click()

    def DropDownButton(self,QUANTITY):
        DropDown=self.driver.find_element(By.XPATH,self.DropDownElement)
        drp= Select(DropDown)
        drp.select_by_visible_text(QUANTITY)
        DropDown.click()


    def InvalidPinCode(self,pcode):
        enterpin = self.driver.find_element(By.XPATH, self.PincodeElement)
        enterpin.send_keys(pcode)



    def Invalid(self):
        Shown = self.driver.find_element(By.XPATH, self.InvalidPin)
        return Shown