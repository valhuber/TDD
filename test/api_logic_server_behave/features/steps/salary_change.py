from behave import *
import requests, pdb
import json
import test_utils

host = "localhost"
port = "5656"

@given('Employee 5 with 95k salary')
def step_impl(context):
    pass

@when('Patch Salary to 200k')
def step_impl(context):
    test_name = "Audit Salary Change"
    test_utils.prt(f'\n\n\n{test_name}... alter salary, ensure audit row created (also available in shell script\n\n', test_name)
    patch_emp_uri = f'http://localhost:5656/api/Employee/5/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "Salary": 200000,
                    "Id": 5},
                "type": "Employee",
                "id": 5
            }}
    r = requests.patch(url=patch_emp_uri, json=patch_args)
    context.response_text = r.text


@then("Salary_audit row created")
def step_impl(context):
    response_text = context.response_text
    assert '"Salary": 200000.0' in response_text, f'Error - "Salary": 200000.0 not in patch response:\n{response_text}'

    audit_uri = f'http://localhost:5656/api/EmployeeAudit/?' \
                'include=Employee&fields%5BEmployeeAudit%5D=Id%2CTitle%2CSalary%2CLastName%2CFirstName%2CEmployeeId%2CCreatedOn&' \
                'page%5Boffset%5D=0&page%5Blimit%5D=10&sort=Id%2CTitle%2CSalary%2CLastName%2CFirstName%2CEmployeeId%2CCreatedOn%2Cid'
    r = requests.get(url=audit_uri)
    response_text = r.text
    assert '"Salary": 200000.0' in response_text, f'Error - "Salary": 200000.0 not in audit response:\n{response_text}'

    test_utils.prt(f'\n then Salary_audit row created... return DB to original state\n')
    patch_emp_uri = f'http://localhost:5656/api/Employee/5/'
    patch_args = \
        {
            "data": {
                "attributes": {
                    "Salary": 95000,
                    "Id": 5},
                "type": "Employee",
                "id": 5
            }}
    r = requests.patch(url=patch_emp_uri, json=patch_args)
    response_text = r.text
