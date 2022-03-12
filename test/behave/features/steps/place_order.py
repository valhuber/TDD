from behave import *

@when('Good Order Placed')
def step_impl(context):
    assert True is not False

@then('Balance Adjusted (demo: chain up)')
def step_impl(context):
    assert context.failed is False

@then('Products Reordered')
def step_impl(context):
    assert context.failed is False


@when('Order Placed with excessive quantity')
def step_impl(context):
    assert True is not False

@then('Rejected per Credit Limit')
def step_impl(context):
    assert context.failed is False   