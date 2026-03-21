from behave import given, when, then
import os
from dashboard import plot

@given('dashboard speed values {values}')
def given_speed_values(context, values):
    context.speed = [int(v) for v in values.split(",")]

@given('dashboard pressure values {values}')
def given_pressure_values(context, values):
    context.pressure = [int(v) for v in values.split(",")]

@when('the plot is generated')
def when_generate_plot(context):
    plot(context.speed, context.pressure)

@then('a plot file should be created')
def then_verify_plot(context):
    assert os.path.exists("plot.png")
