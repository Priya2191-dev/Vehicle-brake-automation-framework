from behave import given, when, then
import os
from plotter import plot

@given('dashboard speed values {values}')
def step_impl(context, values):
    context.speed = [int(v) for v in values.split(",")]

@given('dashboard pressure values {values}')
def step_impl(context, values):
    context.pressure = [int(v) for v in values.split(",")]

@when('the plot is generated')
def step_impl(context):
    plot(context.speed, context.pressure)

@then('a plot file should be created')
def step_impl(context):
    assert os.path.exists("plot.png")
