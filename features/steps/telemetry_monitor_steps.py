from behave import given, when, then
from telemetry_monitor import TelemetryMonitor

@given('a telemetry monitor')
def given_monitor(context):
    context.monitor = TelemetryMonitor()


# Record Single Entry
@when('I record speed {speed} and pressure {pressure}')
def when_record(context, speed, pressure):
    context.monitor.record(int(speed), int(pressure))


@then('one log should be stored')
def then_log_count(context):
    assert len(context.monitor.logs) == 1


@then('the logged speed should be {speed}')
def then_speed(context, speed):
    assert context.monitor.logs[0]["speed"] == int(speed)


@then('the logged pressure should be {pressure}')
def then_pressure(context, pressure):
    assert context.monitor.logs[0]["pressure"] == int(pressure)


@then('the log should contain a timestamp')
def then_timestamp(context):
    assert "timestamp" in context.monitor.logs[0]


# Average Speed
@when('I record multiple telemetry values')
def when_multiple_records(context):
    context.monitor.record(100, 20)
    context.monitor.record(50, 10)


@then('the average speed should be 75')
def then_average(context):
    assert context.monitor.average_speed() == 75


# Invalid Input
@when('I record invalid telemetry data')
def when_invalid(context):
    try:
        context.monitor.record(-10, 20)
    except ValueError as e:
        context.error = e


@then('an telemetry error should be raised')
def then_telemetry_error(context):
    assert isinstance(context.error, ValueError)
