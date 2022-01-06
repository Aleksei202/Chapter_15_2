@wip
Feature: Registration functionality

  @positive
  Scenario: a user inputs valid data for registration
    Given user is on registration page
    When user inputs all data for registration
    Then successful registration info pops up