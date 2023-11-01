# Created by 18327 at 10/28/2023
Feature: Search tests


  Scenario: User can see your cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify your cart is empty message shown


  Scenario: Logged out User can access Sing in
    Given Open target main page
    When Click on Sing in
    When click on Sing in button on the navigation menu
    Then Verify Sign In form opened
    #And verify email field is display
    #And verify password field is display



