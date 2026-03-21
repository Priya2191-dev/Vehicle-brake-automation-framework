from behave import given, when, then
from src.brake_system import validate_brake

@given('dashboard speed values {values}')
def step_speed(context, values):
    context.speed = [int(v) for v in values.split(",")]

@given('dashboard pressure values {values}')
def step_pressure(context, values):
    context.pressure = [int(v) for v in values.split(",")]

@when('the brake validation is performed')
def step_validate(context):
    try:
        context.result = validate_brake(context.speed, context.pressure)
    except Exception:
        context.result = False

@then('braking performance should be valid')
def step_valid(context):
    assert context.result is True

@then('braking performance should be invalid')
def step_invalid(context):
    assert context.result is False
