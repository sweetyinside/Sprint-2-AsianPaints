from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Home_Page:

    def __init__(self, driver):
        self.driver = driver

##--------------> Element locator value / elements property  <--------------------

        self.ShopLinkButton = "//a[@data-target='#SHOP']"
        self.NotNowElement = "//input[@value='Not Now']"
        self.FrameElement = "//*[@id='__st_fancy_popup']/iframe"


##-----------------------> Method for elements <----------------------------------

    def Hover(self):

        # Find the 'SHOP' menu element
        shop_menu = self.driver.find_element(By.XPATH,self.ShopLinkButton )

        # Hover over the menu using ActionChains
        hover = ActionChains(self.driver).move_to_element(shop_menu)
        hover.perform()


    def click_Allow_Button(self):
        Frame = self.driver.find_element(By.XPATH, self.FrameElement)
        self.driver.switch_to.frame(Frame)
        clickAllowButton = self.driver.find_element(By.XPATH, self.NotNowElement)
        clickAllowButton.click()
        time.sleep(6)
        self.driver.switch_to.default_content()