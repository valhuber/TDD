from behave import *

@given('Customer Account: ALFKI')
def step_impl(context):
    pass

@when('GET Customer API')
def step_impl(context):
    import pdb
    pdb.set_trace() # I want to add a break point in here (for whatever reason)
    assert True is not False

@then('ALFKI retrieved')
def step_impl(context):
    assert context.failed is False


@given('Department TBD')
def step_impl(context):
    pass

@when('GET Department with SubDepartments API')
def step_impl(context):
    assert True is not False

@then('SubDepartments returned')
def step_impl(context):
    assert context.failed is False   