# Example

@regression
Feature:Passing parameters to the steps

@smoke @sanity
Scenario: method to passing step parameters
    Given I have a "Apple" in my cart
    And I have a "Mushroom" in my cart
    When I click on "Next"
    And I click on "Finish"
    Then I should see "Error"

@smoke @product
Scenario: method to print the quantity of the product
    Given I have a "10" products in the cart

@product
Scenario: method to print the quantity of the product2
    Given I have a "10" products in the cart2

@product
Scenario: method to print the quantity of the product3
    Given I have a "10" products in the cart3

