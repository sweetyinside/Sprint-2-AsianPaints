from selenium.webdriver.common.by import By


class Shop_Page:

    def __init__(self, driver):
        self.driver = driver

##--------------> Element locator value / elements property  <--------------------

        #self.loginLinkElement = "((//*[@class='iconTextLinks__text visible-in-Desktop'])[6])"
        self.ShopLinkButton = "//a[@data-target='#SHOP']"
        self.ViewAllElement="(//*[@class='ctaText trackCTA'])[1]"
        self.BuyNowElement="/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]"
        #self.ShopLinkElement="((//*[@class='iconTextLinks__text visible-in-Desktop'])[4])"


##-----------------------> Method for elements <----------------------------------


    def click_Shop_link(self):

        #             clicks on shop button

        loginLink = self.driver.find_element(By.XPATH, self.ShopLinkButton)
        loginLink.click()

    def Click_View_All(self):

        #             clicks on View All button

        ViewLink = self.driver.find_element(By.XPATH, self.ViewAllElement)
        #self.driver.execute_script("arguments[0].scrollIntoView();",ViewLink)
        self.driver.execute_script("window.scrollBy(0,2000)")
        ViewLink.click()



    def Switch_Window(self):
        #              switching of window

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    def Buy_Now_Button(self):

        #             clicks on Buy Now button

        Buy_Now = self.driver.find_element(By.XPATH, self.BuyNowElement)
        self.driver.execute_script("window.scrollBy(0,2200)")
        #self.driver.execute_script("arguments[0].scrollIntoView();",Buy_Now)
        Buy_Now.click()









