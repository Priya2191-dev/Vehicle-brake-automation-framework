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


MAX_PRESSURE = 100
MAX_RESPONSE_TIME = 1  # seconds


@given('speed is {speed}')
def step_speed(context, speed):
    context.speed = int(speed)


@given('brake system is OFF')
def step_brake_off(context):
    context.brake_system = False


@given('response time is {time}')
def step_response_time(context, time):
    context.response_time = float(time)


@given('accelerator is ON')
def step_accelerator(context):
    context.accelerator = True


@when('brake is applied with pressure {pressure}')
def step_apply_brake(context, pressure):
    context.pressure = int(pressure)
    context.error = None

    # Validation logic
    if hasattr(context, 'brake_system') and not context.brake_system:
        context.error = "Brake Failure"

    elif context.pressure > MAX_PRESSURE:
        context.error = "Invalid Pressure"

    elif context.speed < 0:
        context.error = "Invalid Speed"

    elif hasattr(context, 'response_time') and context.response_time > MAX_RESPONSE_TIME:
        context.error = "Delay Error"

    elif hasattr(context, 'accelerator'):
        context.priority = "Brake"


@then('vehicle should remain stationary')
def step_stationary(context):
    assert context.speed == 0


@then('vehicle should decelerate safely')
def step_decelerate(context):
    assert context.speed > 0
    assert context.pressure > 0


@then('system should raise error')
def step_invalid_speed(context):
    assert context.error == "Invalid Speed"


@then('system should reject input')
def step_invalid_pressure(context):
    assert context.error == "Invalid Pressure"


@then('alert should be triggered')
def step_brake_failure(context):
    assert context.error == "Brake Failure"


@then('system should flag delay error')
def step_delay(context):
    assert context.error == "Delay Error"


@then('brake should take priority')
def step_priority(context):
    assert context.priority == "Brake"
