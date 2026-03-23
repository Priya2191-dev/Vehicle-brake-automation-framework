from behave import given, when, then
from digital_twin import Vehicle

@given('a vehicle')
def given_vehicle(context):
    context.vehicle = Vehicle()

@given('a vehicle with initial speed {speed}')
def given_vehicle_with_speed(context, speed):
    context.vehicle = Vehicle()
    context.vehicle.speed = float(speed)

@when('the vehicle accelerates by {value}')
def when_accelerate(context, value):
    context.vehicle.accelerate(float(value))

@when('vehicle brake is applied with pressure {pressure}')
def when_apply_brake(context, pressure):
    context.vehicle.apply_brake(float(pressure))

@then('vehicle speed should be {expected}')
def then_verify_speed(context, expected):
    assert round(context.vehicle.speed, 2) == float(expected)

@then('digital twin brake pressure should be {pressure}')
def then_verify_pressure(context, pressure):
    assert context.vehicle.brake_pressure == float(pressure)
