from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("http://automationpractice.com/index.php")

@when('I search for "{query}"')
def step_impl(context, query):
    search_box = context.driver.find_element(By.ID, "search_query_top")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then('I should see results related to "{query}"')
def step_impl(context, query):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".product_list .product-name")
    assert any(query.lower() in product.text.lower() for product in results)