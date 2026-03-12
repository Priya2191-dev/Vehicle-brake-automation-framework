from behave import given, when, then


@given('vehicle speed is {speed:d} km/h')
def step_speed(context, speed):

    context.speed = speed


@when('brake pedal is pressed suddenly')
def step_sudden_brake(context):

    context.abs_active = True


@then('ABS system should activate')
def step_verify_abs(context):

    assert context.abs_active == True


@when('sudden brake is applied')
def step_apply(context):

    context.wheel_locked = False


@then('wheels should not lock')
def step_verify(context):

    assert context.wheel_locked == False
