from behave import given, when, then
from braking import automated_braking

@given('vehicle speed is {speed}')
def given_speed(context, speed):
    context.speed = float(speed)

@given('obstacle distance is {distance}')
def given_distance(context, distance):
    context.distance = float(distance)

@when('system evaluates braking')
def when_evaluate(context):
    context.pressure = automated_braking(context.speed, context.distance)

@then('digital twin brake pressure should be {expected}')
def then_verify_pressure(context, expected):
    assert context.pressure == float(expected)
