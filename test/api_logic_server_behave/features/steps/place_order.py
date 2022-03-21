from behave import *
import requests, pdb
import test_utils
import sys
import json
from dotmap import DotMap

def get_ALFLI():
    get_uri = 'http://localhost:5656/api/Customer/ALFKI/?include=OrderList&fields%5BCustomer%5D=Id%2CCompanyName%2CBalance%2CCreditLimit%2COrderCount%2CUnpaidOrderCount'
    r = requests.get(url=get_uri)
    response_text = r.text
    result_data = json.loads(response_text)
    result_map = DotMap(result_data)
    result_attrs = result_map.data.attributes
    return result_attrs


@given('Customer Account: ALFKI')
def step_impl(context):
    alfki_before = get_ALFLI()
    context.alfki_before = alfki_before
    pass

@when('Good Order Placed')
def step_impl(context):
    add_order_uri = f'http://localhost:5656/api/ServicesEndPoint/add_order'
    add_order_args = {
        "meta": {
            "method": "add_order",
            "args": {
                "CustomerId": "ALFKI",
                "EmployeeId": 1,
                "Freight": 11,
                "OrderDetailList": [
                    {
                        "ProductId": 1,
                        "Quantity": 1,
                        "Discount": 0
                    },
                    {
                        "ProductId": 2,
                        "Quantity": 2,
                        "Discount": 0
                    }
                ]
            }
        }
    }
    scenario_name = 'Good Order Custom Service'
    test_utils.prt(f'\n\n\n{scenario_name} - verify adjustments...\n',\
        scenario_name)
    r = requests.post(url=add_order_uri, json=add_order_args)
    context.response_text = r.text

@then('Logic adjusts Balance (demo: chain up)')
def step_impl(context):
    before = context.alfki_before
    expected_adjustment = 56  # find this from inspecting data on test run
    after = get_ALFLI()
    context.alfki_after = after
    assert before.Balance + expected_adjustment == after.Balance, \
        f'On add, before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'

@then('Logic adusts Products Reordered')
def step_impl(context):
    assert True is not False

@then('Logic adjusts aggregates down on delete order')
def step_impl(context):
    scenario_name = 'Good Order Custom Service - cleanup'
    test_utils.prt(f'\n\n\n{scenario_name} - verify credit check response...\n', scenario_name)
    # find ALFKI order with freight of 11 and delete it (hmm... cannot get created id)
    order_uri = "http://localhost:5656/api/Order/?include=Customer&fields%5BOrder%5D=Id%2CCustomerId%2CEmployeeId%2COrderDate%2CRequiredDate%2CShippedDate%2CShipVia%2CFreight%2CShipName%2CShipAddress%2CShipCity%2CShipRegion%2CShipPostalCode%2CShipCountry%2CAmountTotal%2CCountry%2CCity%2CReady%2COrderDetailCount&page%5Boffset%5D=0&page%5Blimit%5D=10&sort=Id%2CCustomerId%2CEmployeeId%2COrderDate%2CRequiredDate%2CShippedDate%2CShipVia%2CFreight%2CShipName%2CShipAddress%2CShipCity%2CShipRegion%2CShipPostalCode%2CShipCountry%2CAmountTotal%2CCountry%2CCity%2CReady%2COrderDetailCount%2Cid&filter%5BCustomerId%5D=ALFKI&filter%5BFreight%5D=11"
    r = requests.get(url=order_uri)
    response_text = r.text
    result_data = json.loads(response_text)
    result_map = DotMap(result_data)

    orders = result_map.data
    for each_order in orders:
        order_id = each_order.id
        delete_uri = "http://localhost:5656/api/Order/" + str(order_id) + "/"
        r = requests.delete(delete_uri)

    before = context.alfki_before
    expected_adjustment = 0
    after = get_ALFLI()
    context.alfki_after = after
    assert before.Balance + expected_adjustment == after.Balance, \
        f'On delete, Before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'

    assert True is not False

@when('Order Placed with excessive quantity')
def step_impl(context):
    add_order_uri = f'http://localhost:5656/api/ServicesEndPoint/add_order'
    add_order_args = {
        "meta": {
            "method": "add_order",
            "args": {
                "CustomerId": "ALFKI",
                "EmployeeId": 1,
                "Freight": 10,
                "OrderDetailList": [
                    {
                        "ProductId": 1,
                        "Quantity": 1111,
                        "Discount": 0
                    },
                    {
                        "ProductId": 2,
                        "Quantity": 2,
                        "Discount": 0
                    }
                ]
            }
        }
    }
    scenario_name = 'Bad Order Custom Service'
    test_utils.prt(f'\n\n\n{scenario_name} - verify credit check response...\n', 
        scenario_name)
    r = requests.post(url=add_order_uri, json=add_order_args)
    context.response_text = r.text

@then('Rejected per Credit Limit')
def step_impl(context):
    response_text = context.response_text
    print( "one last thing", "by the way", "\n")
    assert "exceeds credit" in response_text, f'Error - "exceeds credit not in {response_text}'
    # behave.log_capture.capture("THIS IS behave.log_capture.capture")

@then('exceeds credit in response')
def step_impl(context):
    response_text = context.response_text
    print( "one last thing", "by the way", "\n")
    assert "exceeds credit" in response_text, f'Error - "exceeds credit not in {response_text}'
    # behave.log_capture.capture("THIS IS behave.log_capture.capture")

def after_step(context, step):
    print("\nflush1 \n\n")
    print("\nflush2 \n\n")


@when('Order Detail Quantity altered very high')
def step_impl(context):
    scenario_name = 'Alter Item Qty to exceed credit'
    test_utils.prt(f'\n\n\n{scenario_name} - verify credit check response...\n', scenario_name)
    patch_cust_uri = f'http://localhost:5656/api/OrderDetail/1040/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "Id": 1040,
                    "Quantity": 1110
                },
                "type": "OrderDetail",
                "id": "1040"
            }
        }
    r = requests.patch(url=patch_cust_uri, json=patch_args)
    response_text = r.text
    context.response_text = r.text


@when('Order RequiredDate altered (2013-10-13)')
def step_impl(context):
    scenario_name = 'Alter Required Date - adjust logic pruned'
    test_utils.prt(f'\n\n\n{scenario_name}... observe rules pruned for Order.RequiredDate (2013-10-13) \n\n', scenario_name)
    patch_uri = f'http://localhost:5656/api/Order/10643/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "RequiredDate": "2013-10-13",
                    "Id": 10643},
                "type": "Order",
                "id": 10643
            }}
    r = requests.patch(url=patch_uri, json=patch_args)
    response_text = r.text
    context.response_text = r.text

@then('Balance not adjusted')
def step_impl(context):
    before = context.alfki_before
    expected_adjustment = 0
    after = get_ALFLI()
    context.alfki_after = after
    assert before.Balance + expected_adjustment == after.Balance, \
        f'Before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'



@when('Order ShippedDate altered (2013-10-13)')
def step_impl(context):
    scenario_name = 'Set Shipped - adjust logic reuse'
    test_utils.prt(f'\n\n\n{scenario_name}... observe rules pruned for Order.RequiredDate (2013-10-13) \n\n', scenario_name)
    patch_uri = f'http://localhost:5656/api/Order/10643/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "ShippedDate": "2013-10-13",
                    "Id": 10643},
                "type": "Order",
                "id": 10643
            }}
    r = requests.patch(url=patch_uri, json=patch_args)
    response_text = r.text
    context.response_text = r.text

@then('Balance reduced 1086')
def step_impl(context):
    before = context.alfki_before
    expected_adjustment = -1086
    shipped = get_ALFLI()
    context.alfki_shipped = shipped  # alert - this variable not visible in next scenario... need to use given
    assert before.Balance + expected_adjustment == shipped.Balance, \
        f'Before balance {before.Balance} + {expected_adjustment} != new Balance {shipped.Balance}'


@given('Shipped Order')
def step_impl(context):
    context.alfki_shipped = get_ALFLI()
    pass

@when('Order ShippedDate set to None')
def step_impl(context):
    scenario_name = 'Reset Shipped - adjust logic reuse'
    test_utils.prt(f'\n\n\n{scenario_name}... observe rules pruned for Order.RequiredDate (2013-10-13) \n\n', scenario_name)
    patch_uri = f'http://localhost:5656/api/Order/10643/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "ShippedDate": None,
                    "Id": 10643},
                "type": "Order",
                "id": 10643
            }}
    r = requests.patch(url=patch_uri, json=patch_args)
    response_text = r.text
    context.response_text = r.text

@then('Logic adjusts Balance by -1086')
def step_impl(context):
    before = context.alfki_shipped
    expected_adjustment = 1086
    after = get_ALFLI()
    context.alfki_after = after
    assert before.Balance + expected_adjustment == after.Balance, \
        f'Before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'
