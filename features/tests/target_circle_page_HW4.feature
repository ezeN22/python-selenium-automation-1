# Created by 18327 at 11/4/2023
Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target main page
    When Click target circle
    Then Verify header has 5 benefit