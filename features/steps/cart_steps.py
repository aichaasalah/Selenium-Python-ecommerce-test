from behave import when, then
from selenium.webdriver.common.by import By
import time

@when('I search and add "{product}" to the cart')
def step_impl(context, product):
    search_box = context.driver.find_element(By.ID, "search_query_top")
    search_box.clear()
    search_box.send_keys(product)
    search_box.submit()
    time.sleep(2)
    product_link = context.driver.find_element(By.CSS_SELECTOR, ".product_list .product-name")
    product_link.click()
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add_to_cart")
    add_button.click()
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, ".button-container a[title='Proceed to checkout']").click()

@then('the product should appear in the cart summary')
def step_impl(context):
    summary = context.driver.find_element(By.ID, "cart_summary")
    rows = summary.find_elements(By.CSS_SELECTOR, ".cart_description .product-name")
    assert len(rows) > 0