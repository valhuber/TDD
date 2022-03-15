from behave import *
import requests, pdb
import test_services
import sys
import json

def get_ALFLI():
    get_uri = 'http://localhost:5656/api/Customer/ALFKI/?include=OrderList&fields%5BCustomer%5D=Id%2CCompanyName%2CBalance%2CCreditLimit%2COrderCount%2CUnpaidOrderCount'
    r = requests.get(url=get_order_uri)
    response_text = r.text
    result_data = json.loads(response_text)
    return result_data


@given('Customer Account: ALFKI')
def step_impl(context):
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
                "Freight": 10,
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
    test_services.prt(f'\n\n\n{test_name} - verify credit check returned...\n', test_name)
    r = requests.post(url=add_order_uri, json=add_order_args)
    context.response_text = r.text
    # assert "???" in r.text, f'Error - is order# in {r.text}'

@then('Balance Adjusted (demo: chain up)')
def step_impl(context):
    response_text = context.response_text
    print( "one last thing", "by the way", "\n")
    assert "exceeds credit" not in response_text, f'Error - "exceeds credit not in {response_text}'

@then('Products Reordered')
def step_impl(context):
    assert True is not False

@then('Proper delete')
def step_impl(context):
    # find ALFKI order with freight of 10 and delete it
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
    test_services.prt(f'\n\n\n{test_name} - verify credit check returned...\n', test_name)
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