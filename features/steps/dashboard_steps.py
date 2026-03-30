from behave import given, when, then
import os
from dashboard import plot

@given('dashboard speed values {values}')
def given_speed(context, values=None):
    context.speed = [int(v.strip()) for v in values.split(",")]
    
@given('dashboard pressure values {values}')
def given_pressure(context, values=None):
    context.pressure = [int(v.strip()) for v in values.split(",")]
    
@given('dashboard speed values')
def given_empty_speed(context):
    context.speed = []

@given('dashboard pressure values')
def given_empty_pressure(context):
    context.pressure = []


@when('the plot is generated')
def when_plot(context):
    plot(context.speed, context.pressure)

@when('the plot is generated with invalid data')
def when_invalid_plot(context):
    try:
        plot(context.speed, context.pressure)
    except ValueError as e:
        context.error = e


@then('a plot file should be created')
def then_file_created(context):
    assert os.path.exists("plot.png")

@then('an dashboard error should be raised')
def then_dashboard_error(context):
    assert isinstance(context.error, ValueError)
