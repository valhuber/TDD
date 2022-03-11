from behave import *

@given('we can do 2 tests')
def step_impl(context):
    pass

@when('when tomorrow comes')
def step_impl(context):
    assert True is not False

@then('it will be good')
def step_impl(context):
    assert context.failed is False

@given('the sun sets in the west')
def step_impl(context):
    pass
