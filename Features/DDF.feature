Feature: Excel sheet

    Background: Entering data with Excel sheet
    Given Chrome is opened and Asian Paints app is opened


  Scenario: Validate BUY NOW functionality with valid data

    When User hovers over Shop link
    And User clicks on Shop link
    And User clicks on BUY NOW
    Then User navigates to BUY NOW page
    And User scrolls the page down
    When User tries to enter the valid <Pincode> to check the delivery service
    And User tries to clicks on ADD TO CART