import time
from hamcrest import *
from behave import *
from datafiles import ExcelUtils
from selenium.webdriver.common.by import By

from Features.Pages.P_03_BuyNowPage import BuyNow_Page
from Features.Utility.ConfigClass import ConfigClass



@when("User tries to enter the valid {Pincode} to check the delivery service")
def step_impl(context,Pincode):

    ExcelUtils.get_row_count(ConfigClass.datafilePath, "Sheet1")

    Pincode = ExcelUtils.read_data(ConfigClass.datafilePath, "Sheet1", 2, 1)

    ExcelPincode = BuyNow_Page(context.driver)
    ExcelPincode.InvalidPinCode(Pincode)



@step("User tries to clicks on ADD TO CART")
def step_impl(context):
    time.sleep(3)
    Buy = BuyNow_Page(context.driver)
    Buy.clickaddtocart()
    time.sleep(3)

    Pin = BuyNow_Page(context.driver)

    if (Pin.Invalid()):
        assert True
        print("Test is passed and Error is visible")
        ExcelUtils.write_data(ConfigClass.datafilePath, "Sheet1", 2, 2, "Passed")
    else:
        print("Test is failed and Error is not visible")
        ExcelUtils.write_data(ConfigClass.datafilePath, "Sheet1", 2, 2, "Failed")
        assert False
    time.sleep(2)