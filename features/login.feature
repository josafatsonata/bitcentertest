# Created by blueikari at 7/24/19
Feature: Test suite for the user login and register page

  Scenario: Login basic flow
    Given I am on the homepage
    When I click the login button in the home page
    Then I enter "josafat@behave.prg" into the "email" field
    Then I enter "password" into the "password" field
    And I wait "2" seconds
    Then I close the browser


   Scenario: Login wrong email
    Given I am on the homepage
    When I click the login button in the home page
    Then I enter "josafat@behave.org" into the "email" field
    Then I enter "password" into the "password" field
    When I click the submit button
    Then I verify that the error message displays
    And I wait "2" seconds
    Then I close the browser