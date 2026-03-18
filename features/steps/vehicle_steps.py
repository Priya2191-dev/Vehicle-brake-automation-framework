from behave import given, when, then
from vehicle import Vehicle

@given('a vehicle')
def step_impl(context):
    context.vehicle = Vehicle()

@given('a vehicle with initial speed {speed}')
def step_impl(context, speed):
    context.vehicle = Vehicle()
    context.vehicle.speed = float(speed)

@when('the vehicle accelerates by {value}')
def step_impl(context, value):
    context.vehicle.accelerate(float(value))

@when('brake is applied with pressure {pressure}')
def step_impl(context, pressure):
    context.vehicle.apply_brake(float(pressure))

@then('vehicle speed should be {expected}')
def step_impl(context, expected):
    assert round(context.vehicle.speed, 2) == float(expected)

@then('brake pressure should be {pressure}')
def step_impl(context, pressure):
    assert context.vehicle.brake_pressure == float(pressure)
