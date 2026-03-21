from behave import given, when, then
from telemetry_monitor import TelemetryMonitor  

@given('a telemetry monitor')
def given_telemetry_monitor(context):
    context.monitor = TelemetryMonitor()

@when('I record speed {speed} and pressure {pressure}')
def when_record_data(context, speed, pressure):
    context.monitor.record(int(speed), int(pressure))

@then('one log should be stored')
def then_verify_log_count(context):
    assert len(context.monitor.logs) == 1

@then('the logged speed should be {speed}')
def then_verify_speed(context, speed):
    assert context.monitor.logs[0]["speed"] == int(speed)

@then('the logged pressure should be {pressure}')
def then_verify_pressure(context, pressure):
    assert context.monitor.logs[0]["pressure"] == int(pressure)
