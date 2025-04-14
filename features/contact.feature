Feature: Contact Us Form

  Scenario: Send a contact form
    Given I am on the contact page
    When I fill in the contact form with valid data
    Then I should see a success message
