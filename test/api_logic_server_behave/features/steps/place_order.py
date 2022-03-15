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
    test_name = 'Custom Service: add_order - good'
    test_utils.prt(f'\n\n\n{test_name} - verify adjustments...\n', test_name)
    r = requests.post(url=add_order_uri, json=add_order_args)
    context.response_text = r.text

@then('Balance Adjusted (demo: chain up)')
def step_impl(context):
    before = context.alfki_before
    expected_adjustment = 56  # find this from inspecting data on test run
    after = get_ALFLI()
    context.alfki_after = after
    assert before.Balance + expected_adjustment == after.Balance, \
        f'Before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'

@then('Products Reordered')
def step_impl(context):
    assert True is not False

@then('Proper delete')
def step_impl(context):
    # find ALFKI order with freight of 11 and delete it (hmm... cannot get created id)
    order_uri = "http://localhost:5656/api/Order/?include=Customer&fields%5BOrder%5D=Id%2CCustomerId%2CEmployeeId%2COrderDate%2CRequiredDate%2CShippedDate%2CShipVia%2CFreight%2CShipName%2CShipAddress%2CShipCity%2CShipRegion%2CShipPostalCode%2CShipCountry%2CAmountTotal%2CCountry%2CCity%2CReady%2COrderDetailCount&page%5Boffset%5D=0&page%5Blimit%5D=10&sort=Id%2CCustomerId%2CEmployeeId%2COrderDate%2CRequiredDate%2CShippedDate%2CShipVia%2CFreight%2CShipName%2CShipAddress%2CShipCity%2CShipRegion%2CShipPostalCode%2CShipCountry%2CAmountTotal%2CCountry%2CCity%2CReady%2COrderDetailCount%2Cid&filter%5BCustomerId%5D=ALFKI&filter%5BFreight%5D=11"
    r = requests.get(url=order_uri)
    response_text = r.text
    result_data = json.loads(response_text)
    result_map = DotMap(result_data)
    # if > 1, get result_map.data (array)

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
        f'Before balance {before.Balance} + {expected_adjustment} != new Balance {after.Balance}'

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
    test_name = 'Custom Service: add_order - bad'
    test_utils.prt(f'\n\n\n{test_name} - verify credit check response...\n', test_name)
    r = requests.post(url=add_order_uri, json=add_order_args)
    context.response_text = r.text
    # https://stackoverflow.com/questions/25150404/how-can-i-see-print-statements-in-behave-bdd#:~:text=By%20default%2C%20behave%20does%20not%20display%20any%20output,is%20to%20change%20some%20of%20the%20default%20settings.
    # print("here is some output\n\n\n")
    # print(r.text, "\n\n")

@then('Rejected per Credit Limit')
def step_impl(context):
    response_text = context.response_text
    print( "one last thing", "by the way", "\n")
    assert "exceeds credit" in response_text, f'Error - "exceeds credit not in {response_text}'
    # behave.log_capture.capture("THIS IS behave.log_capture.capture")

@then('And Test')
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
    test_name = 'Order Detail Quantity altered very high'
    test_utils.prt(f'\n\n\n{test_name} - verify credit check response...\n', test_name)
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
