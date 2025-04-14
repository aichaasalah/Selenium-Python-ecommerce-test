Feature: Login

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I try to login with invalid email and password
    Then I should see an error message
