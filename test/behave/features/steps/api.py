from behave import *
import requests, pdb

host = "localhost"
port = "5656"

@given('Customer Account: ALFKI')
def step_impl(context):
    pass

@when('GET Customer API')
def step_impl(context):
    # pdb.set_trace() # I want to add a break point in here (for whatever reason)
    # todo - host and port hard-coded
    get_order_uri = f'http://localhost:5656/api/Order/?' \
                f'fields%5BOrder%5D=Id%2CCustomerId%2CEmployeeId%2COrderDate%2CAmountTotal' \
                f'&page%5Boffset%5D=0&page%5Blimit%5D=10&filter%5BId%5D=10248'
    r = requests.get(url=get_order_uri)
    response_text = r.text
    context.response_text = response_text
    assert True is not False

@then('ALFKI retrieved')
def step_impl(context):
    response_text = context.response_text
    assert "VINET" in response_text, f'Error - "VINET not in {response_text}'


@given('Department TBD')
def step_impl(context):
    pass

@when('GET Department with SubDepartments API')
def step_impl(context):
    assert True is not False

@then('SubDepartments returned')
def step_impl(context):
    assert context.failed is False   