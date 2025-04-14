from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('I am on the login page')
def step_impl(context):
    context.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

@when('I try to login with invalid email and password')
def step_impl(context):
    context.driver.find_element(By.ID, "email").send_keys("invalid@example.com")
    context.driver.find_element(By.ID, "passwd").send_keys("wrongpassword")
    context.driver.find_element(By.ID, "SubmitLogin").click()

@then('I should see an error message')
def step_impl(context):
    error = context.driver.find_element(By.CSS_SELECTOR, ".alert-danger")
    assert "authentication failed" in error.text.lower()
