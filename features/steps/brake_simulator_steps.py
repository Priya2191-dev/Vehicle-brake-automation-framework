from behave import given, when, then
from brake_simulator import BrakeSimulator   

@given('a vehicle with speed {speed}')
def given_vehicle_speed(context, speed):
    context.simulator = BrakeSimulator(float(speed))

@when('brake is applied with pressure {pressure}')
def when_apply_brake(context, pressure):
    context.new_speed = context.simulator.apply_brake(float(pressure))

@then('the new speed should be {expected}')
def then_verify_speed(context, expected):
    assert round(context.new_speed, 2) == float(expected)
