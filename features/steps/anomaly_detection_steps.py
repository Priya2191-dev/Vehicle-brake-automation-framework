from behave import given, when, then
from anomaly_detection import detect_anomaly   

@given('speed values {values}')
def step_impl(context, values):
    context.speeds = [int(v.strip()) for v in values.split(",")]

@when('anomaly detection is performed')
def step_impl(context):
    context.result = detect_anomaly(context.speeds)

@then('anomaly should be detected')
def step_impl(context):
    assert context.result is True

@then('no anomaly should be detected')
def step_impl(context):
    assert context.result is False
