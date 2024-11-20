from behave import *


@given('user enters name and password')
def step_impl(context):
    # access multiline text with .text attribute
    print("Multiline Text: " + context.text)


@then('user should be logged in')
def step_impl(context):
    print(context)
