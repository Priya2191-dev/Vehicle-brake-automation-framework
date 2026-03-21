from behave import given, when, then
from braking import automated_braking

@given('vehicle speed is 80')
def given_speed(context):
    context.speed = 80

@given('obstacle distance is 5')
def given_distance(context):
    context.distance = 5

@when('system evaluates braking')
def when_evaluate(context):
    context.pressure = automated_braking(context.speed, context.distance)

@then('brake pressure should be 40')
def then_verify_pressure(context):
    assert context.pressure == 40
