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
    | Dell XPS 13 (2020) Laptop | $1,398.98 |


Scenario Outline: Add to shopping cart
    Given The site has product <product> with price <price>
    When I am on the <product> page
    Then I can add the product to the shopping cart

    Examples:
    | product                   | price     |
    | Dell XPS 13 (2020) Laptop | $1,398.98 |
