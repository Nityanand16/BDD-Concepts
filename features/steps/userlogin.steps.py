from behave import given, when, then


@given(u'I login as a "{role}"')
def i_login_as(context, role):
    print(f"I am with role {role}")


@then(u'I should be at "{page}"')
def i_should_be_at_page(context, page):
    print(f"I am at page {page}")

#
# @given(u'I login as a "{role}"')
# def i_login_as(context, role):
#     print(f"I am with role {role}")
#
#
# @then(u'I should be at "{page}"')
# def i_should_be_at_page(context, page):
#     print(f"I am at page {page}")
#
#
# @given(u'I login as a "{role}"')
# def i_login_as(context, role):
#     print(f"I am with role {role}")
#
#
# @then(u'I should be at "{page}"')
# def i_should_be_at_page(context, page):
#     print(f"I am at page {page}")
#