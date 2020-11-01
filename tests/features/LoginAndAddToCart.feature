@ui
Feature: E-Commerce site interactions

Scenario: Unsuccessful Login
    Given I don't have valid username and password
    When I try to login
    Then I get message "Login was unsuccessful"


Scenario Outline: Product Search
    Given The site has product <product> with price <price>
    When I search for <product>
    Then I can find <product> page
    And I can see the price <price>

    Examples:
    | product                   | price     |  
    | Asus N551JK-XO076H Laptop | $1,500.00 |


Scenario Outline: Add to shopping cart
    Given The site has product <product> with price <price>
    When I am on the <product> page
    Then I can add the product to the shopping cart

    Examples:
    | product                   | price     |  
    | Asus N551JK-XO076H Laptop | $1,500.00 |
