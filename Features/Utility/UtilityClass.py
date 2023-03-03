from selenium import webdriver

from Features.Pages.P_01_HomePage import Home_Page
from Features.Utility.ConfigClass import ConfigClass
from selenium.webdriver.chrome.options import Options

class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)
        self.driver.maximize_window()

    def launch_browser_notification(self):
        chromeOptions = Options()

        chromeOptions.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(ConfigClass.filePath, chrome_options=chromeOptions)


    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()