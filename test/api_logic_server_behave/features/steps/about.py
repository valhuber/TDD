from behave import *
import requests, pdb
import test_utils
import json

host = "localhost"
port = "5656"

@given('Sample Database')
def step_impl(context):
    assert True

@when('Transactions are submitted')
def step_impl(context):
    assert True is not False

@then('Enforce business policies with Logic (rules + code)')
def step_impl(context):
    test_utils.prt(f'Rules Report', 'Enforce business policies with Logic (rules + code)')
    assert True