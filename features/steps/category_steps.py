from behave import when, then
from selenium.webdriver.common.by import By
import time

@when('I navigate to the "Women" category')
def step_impl(context):
    women_link = context.driver.find_element(By.LINK_TEXT, "Women")
    women_link.click()
    time.sleep(2)

@then('I should see the product list for women')
def step_impl(context):
    heading = context.driver.find_element(By.CLASS_NAME, "cat-name")
    assert "WOMEN" in heading.text.upper()
