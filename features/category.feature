Feature: Browse by Category

  Scenario: Open the Women category
    Given I am on the homepage
    When I navigate to the "Women" category
    Then I should see the product list for women
