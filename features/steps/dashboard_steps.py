from behave import given, when, then
import os
from dashboard import plot

@given('dashboard speed values {values}')
def given_speed(context, values=None):
    if values:
        context.speed = [int(v.strip()) for v in values.split(",")]
    else:
        context.speed = []

@given('dashboard pressure values {values}')
def given_pressure(context, values=None):
    if values:
        context.pressure = [int(v.strip()) for v in values.split(",")]
    else:
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


@then('an error should be raised')
def then_error(context):
    assert isinstance(context.error, ValueError)
