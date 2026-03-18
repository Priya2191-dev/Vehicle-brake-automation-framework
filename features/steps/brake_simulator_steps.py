from behave import given, when, then
from brake_simulator import BrakeSimulator   

@given('a vehicle with speed {speed}')
def step_impl(context, speed):
    context.simulator = BrakeSimulator(float(speed))

@when('brake is applied with pressure {pressure}')
def step_impl(context, pressure):
    context.new_speed = context.simulator.apply_brake(float(pressure))

@then('the new speed should be {expected}')
def step_impl(context, expected):
    assert round(context.new_speed, 2) == float(expected)
