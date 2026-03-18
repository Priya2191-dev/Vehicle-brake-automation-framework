from behave import given, when, then
from telemetry_monitor import TelemetryMonitor  

@given('a telemetry monitor')
def step_impl(context):
    context.monitor = TelemetryMonitor()

@when('I record speed {speed} and pressure {pressure}')
def step_impl(context, speed, pressure):
    context.monitor.record(int(speed), int(pressure))

@then('one log should be stored')
def step_impl(context):
    assert len(context.monitor.logs) == 1

@then('the logged speed should be {speed}')
def step_impl(context, speed):
    assert context.monitor.logs[0]["speed"] == int(speed)

@then('the logged pressure should be {pressure}')
def step_impl(context, pressure):
    assert context.monitor.logs[0]["pressure"] == int(pressure)
