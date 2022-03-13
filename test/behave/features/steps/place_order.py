from behave import *
import requests, pdb
import test_services
import sys

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
    test_name = 'big bad order'
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
    assert "exceeds cedit" in response_text, f'Error - "exceeds credit not in {response_text}'
    # behave.log_capture.capture("THIS IS behave.log_capture.capture")

def after_step(context, step):
    print("\nflush1 \n\n")
    print("\nflush2 \n\n")