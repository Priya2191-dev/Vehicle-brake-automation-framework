from behave import given, when, then
from src.braking import automated_braking

@given('vehicle speed is 80')
def step(context):
    context.speed = 80

@given('obstacle distance is 5')
def step(context):
    context.distance = 5

@when('system evaluates braking')
def step(context):
    context.pressure = automated_braking(context.speed, context.distance)

@then('brake pressure should be 40')
def step(context):
    assert context.pressure == 40
