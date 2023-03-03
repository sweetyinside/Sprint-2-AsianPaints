import time
from Features.Utility.UtilityClass import UtilityClass

def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    context.driver.implicitly_wait(3)
    UtilityClass.launch_app(context)
    context.driver.implicitly_wait(3)

def after_scenario(context, driver):
    context.driver.implicitly_wait(3)
    UtilityClass.close_browser(context)
