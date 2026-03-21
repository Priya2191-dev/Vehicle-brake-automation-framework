from behave import given, when, then
from brake_system import validate_brake

@given('brake system speed values {values}')
def given_speed(context, values):
    context.speed = [int(v) for v in values.split(",")]

@given('brake system pressure values {values}')
def given_pressure(context, values):
    context.pressure = [int(v) for v in values.split(",")]

@when('the brake validation is performed')
def when_brake_validate(context):
    try:
        context.result = validate_brake(context.speed, context.pressure)
    except Exception:
        context.result = False

@then('braking performance should be valid')
def then_brake_performance_valid(context):
    assert context.result is True

@then('braking performance should be invalid')
def then_brake_performance_invalid(context):
    assert context.result is False
