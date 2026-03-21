from behave import given, when, then
from anomaly_detection import detect_anomaly   

@given('speed values {values}')
def given_speed_values(context, values):
    context.speeds = [int(v.strip()) for v in values.split(",")]

@when('anomaly detection is performed')
def when_run_anomaly_detection(context):
    context.result = detect_anomaly(context.speeds)

@then('anomaly should be detected')
def then_verify_anomaly(context):
    assert context.result is True

@then('no anomaly should be detected')
def then_verify_no_anomaly(context):
    assert context.result is False
