Feature: Product Search

  Scenario: Search for an existing product
    Given I am on the homepage
    When I search for "dress"
    Then I should see results related to "dress"
