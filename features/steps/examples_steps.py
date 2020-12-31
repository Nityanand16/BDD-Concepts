# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

# from behave import given ,then , when
# import  logging as logger
# from behave.__main__ import main as behave_main
# from behave.configuration import ConfigError
#
#
# try:
#     behave_main('path/to/feature_file.feature -f json -o /path/to/logs/here')
# except ConfigError:
#     print("Caught it!")
#
#
# @given('I am on loginpage')
# def user_on_login_page(context):
#     print("user on login page")
#     logger.info("hello")
#
# @when('I type my email')
# def add_crednetials(context):
#     print('I have entered valida credentials and password')
#
# @when('I type my password')
# def add_crednetialss(context):
#     print('I have entered valida credentials and passwords')
#
# @when('I click on login button')
# def add_crednetialss(context):
#     print('I have entered valida credentials and passwords')
#
# @then('I should see welcome text')
# def verify_dashboard(context):
#     print('I can see the welcome message')
#     #assert 5 == 6 ,'5 not equal to six'


# behave
# behave example.feature
# behave -h
# behave --no-capture-stderr
# behave --no-logcapture



