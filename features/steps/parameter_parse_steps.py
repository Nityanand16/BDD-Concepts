from behave import given , then , when


@given('I have a {item} in my cart')
def i_have_item_in_cart(context,item):
    print("The item is :{}".format(item))
    #print(f'The item is {item}')

@when('And I have a {text} in my cart')
def i_have_item_in_cart_Another(context,text):
    print("The item is :{}".format(text))
    print(f'The item is {text}')
    print(context.text)

@when('I click on {x}')
def i_hve(context,x):
    print("The item is :{}".format(x))
    print(f'The item is {x}')


@when(' I click on {y}')
def i_have_item_in_car_Next_Finish(context,y):
    print("The item is :{}".format(y))
    print(f'The item is {y}')

@then('I should see {z}')
def i_have_item_in_car_Next_Finish_end(context,z):
    print("The item is :{}".format(z))
    print(f'The item is {z}')


@given('I have a {} products in the cart')
def i_have_number_items_products_in_cart(context,y):
    print("The item is :{}".format(y))

@given('I have a {} products in the cart2')
def i_have_number_items_products_in_cartw(context,y):
    print("The item is :{}".format(y))

@given('I have a {} products in the cart3')
def i_have_number_items_products_in_carty(context,y):
    print("The item is :{}".format(y))