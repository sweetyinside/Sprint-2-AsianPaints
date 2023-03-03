import time
from behave import *
from hamcrest import *
from Features.Pages.P_02_Shop_Page import Shop_Page
from Features.Pages.P_03_BuyNowPage import BuyNow_Page
from Features.Pages.P_01_HomePage import Home_Page


##########################################################################################
##SNERAIO-->1


@given(u'Chrome is opened and Asian Paints app is opened')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title of SCENARIO-1 is--> " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when("User clicks on NotNow- Notification")
def step_impl(context):
    context.driver.implicitly_wait(3)
    Allowvalue = Home_Page(context.driver)
    Allowvalue.click_Allow_Button()
    time.sleep(3)


@step(u'User hovers over Shop link')
def step_impl(context):
    time.sleep(3)
    hover = Home_Page(context.driver)
    hover.Hover()
    context.driver.implicitly_wait(3)


@then(u'It Shows the list of the categories')
def step_impl(context):                     #//dropdown-menu__container--list-holder
    time.sleep(3)


########################################################################################
## SCENARIO-->2

@when("User clicks on Shop link")
def step_impl(context):
    time.sleep(3)
    ShopButton = Shop_Page(context.driver)
    ShopButton.click_Shop_link()

@then(u'It navigates to the Shop page')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Wall Stickers, Home and Personal Hygiene, DIY, Mask and PPE, Wallpaper, Colour Selection & Mechanized Tools - Asian Paints Online-Shop"
    actualTitle = context.driver.title
    print("Page title of SCENARIO-2 is--> " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)

############################################################################
## SCENARIO-->3

@when("User clicks on View all Button")
def step_impl(context):
    time.sleep(3)
    ViewAllButton = Shop_Page(context.driver)
    ViewAllButton.Click_View_All()
    time.sleep(3)


@then(u'It navigates user to the View All page')
def step_impl(context):

    time.sleep(3)
    New_Window=Shop_Page(context.driver)
    New_Window.Switch_Window()
    time.sleep(3)
    expectedTitle = "Decorative Wall Stickers & Wall Decals For Home Walls - Asian Paints"
    actualTitle = context.driver.title
    print("Page title of SCENARIO-3 is--> " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)


#######################################################################################
## SCENARIO-->4

@step("User clicks on BUY NOW")
def step_impl(context):
    time.sleep(3)
    Buy = Shop_Page(context.driver)
    Buy.Buy_Now_Button()
    time.sleep(3)


@then(u'User navigates to BUY NOW page')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Asian Paints Colour Cosmos Fan Deck 2200 Colours"
    actualTitle = context.driver.title
    print("Page title of SCENARIO-4 is--> " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)


@step("User scrolls the page down")
def step_impl(context):
    time.sleep(3)
    scrolldown=BuyNow_Page(context.driver)
    scrolldown.scroll_page()
    time.sleep(3)


@when("User enters the valid {PINCODE} to check the delivery service")
def step_impl(context, PINCODE):
    time.sleep(3)
    pin = BuyNow_Page(context.driver)
    pin.enter_pincode_textbox(PINCODE)


@step("User clicks on ADD TO CART")
def step_impl(context):
    time.sleep(3)
    Buy = BuyNow_Page(context.driver)
    Buy.clickaddtocart()
    time.sleep(3)


@then("It gives the message based on the service and pincode")
def step_impl(context):
    pass



@when("User Selects the {QUANTITY} of the item from the dropdown")
def step_impl(context, QUANTITY):
    time.sleep(3)
    pin = BuyNow_Page(context.driver)
    pin.DropDownButton(QUANTITY)


##################################################################################
## SCENARIO-->5

@when("User enters the Invalid {PINCODE} to check the delivery service")
def step_impl(context, PINCODE):
    time.sleep(3)
    pin = BuyNow_Page(context.driver)
    pin.InvalidPinCode(PINCODE)
    print("Please enter valid pincode")


#####################################################################################