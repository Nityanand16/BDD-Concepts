
from behave import given , when, then

@given('I find the random order from the database')
def find_order_from_db(context):
    print('Finding the order number from a db')
    print(context.order_number)


#-----------------------------------------------

@when('I initiate the refund for the order')
def find_order_from_db_2(context):
    print('Finding the order number from a db')
    print(context.order_number)

#------------------------------------------------
@then('The payment should get processed for the user')
def find_order_from_db_3(context):

    print('Finding the order number from a db')
    print(context.order_number)


@when(u'I issue a refund on the same order')
def a(context):
    print(context.order_number)


@then(u'the refund should fail')
def a(context):
    print(context.order_number)




