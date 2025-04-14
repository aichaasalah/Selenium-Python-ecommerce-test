from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@given('I am on the contact page')
def step_impl(context):
    context.driver.get("http://automationpractice.com/index.php?controller=contact")

@when('I fill in the contact form with valid data')
def step_impl(context):
    subject = Select(context.driver.find_element(By.ID, "id_contact"))
    subject.select_by_visible_text("Customer service")
    context.driver.find_element(By.ID, "email").send_keys("test@example.com")
    context.driver.find_element(By.ID, "message").send_keys("Hello, I need help with my order.")
    context.driver.find_element(By.ID, "submitMessage").click()

@then('I should see a success message')
def step_impl(context):
    success = context.driver.find_element(By.CSS_SELECTOR, ".alert-success")
    assert "successfully" in success.text.lower()

