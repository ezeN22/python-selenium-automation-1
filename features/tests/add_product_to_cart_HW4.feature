# Created by 18327 at 11/6/2023
Feature: Users can add a product to cart


  Scenario: Users can add a product to cart
    Given open target main page
    When search for a bag
    And click on the product
    And store product name
    And click on add to cart button
    And open cart page
    Then verify cart has 1 item(s)
    And verify cart has correct product


