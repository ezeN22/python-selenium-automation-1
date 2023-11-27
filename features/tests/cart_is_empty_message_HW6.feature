# Created by 18327 at 11/27/2023
Feature: Search tests

  Scenario: User can see your cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty message shown
