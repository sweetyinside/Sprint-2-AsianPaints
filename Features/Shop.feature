Feature: Shop Page

  Background: Asian Paint Navigation
    Given Chrome is opened and Asian Paints app is opened
    When User clicks on NotNow- Notification
    And User hovers over Shop link


  Scenario: Successfully Hovering over Shop link
    #When User hovers on shop
    Then It Shows the list of the categories


  Scenario: Successful navigation on Shop Page
    When User clicks on Shop link
    Then It navigates to the Shop page


  Scenario: Successful navigation on View All page
    When User clicks on Shop link
    Then It navigates to the Shop page
    When User clicks on View all Button
    Then It navigates user to the View All page



  Scenario Outline: Validate BUY NOW functionality with valid data
    When User clicks on Shop link
    And User clicks on BUY NOW
    Then User navigates to BUY NOW page
    And User scrolls the page down
    When User enters the valid <PINCODE> to check the delivery service
    And User clicks on ADD TO CART
    Then It gives the message based on the service and pincode

    Examples:
      | PINCODE |
      | 560047 |
      | 824143 |



  Scenario Outline: Validate BUY NOW functionality with invalid data
    When User clicks on Shop link
    And User clicks on BUY NOW
    Then User navigates to BUY NOW page
    And User scrolls the page down
    When User enters the Invalid <PINCODE> to check the delivery service
    And User clicks on ADD TO CART
    Then It gives the message based on the service and pincode

    Examples:
      | PINCODE |
      | 57842 |
      | 23656 |


