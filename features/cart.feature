Feature: Shopping Cart

  Scenario: Add product to cart
    Given I am on the homepage
    When I search and add "Printed Dress" to the cart
    Then the product should appear in the cart summary
