from behave import given, when, then
import logging as logger


@given('I am on loginpage')
def user_on_login_page(context):
    print("user on login page")
    logger.info("hello")

@when('I type my email')
def add_crednetials(context):
    print('I have entered valida credentials and password')

@when('I type my password')
def add_crednetialss(context):
    print('I have entered valida credentials and passwords')

@when('I click on login button')
def add_crednetialss(context):
    print('I have entered valida credentials and passwords')

@then('I should see welcome text')
def verify_dashboard(context):
    print('I can see the welcome message')
    #assert 5 == 6 ,'5 not equal to six'
