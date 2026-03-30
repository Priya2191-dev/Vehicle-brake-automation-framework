from behave import given, when, then
from anomaly_detection import detect_anomaly

@given('data values {values}')
def given_data(context, values=None):
    if values:
        context.data = [int(v.strip()) for v in values.split(",")]
    else:
        context.data = []


@when('anomaly detection is performed')
def when_detect(context):
    context.result = detect_anomaly(context.data)


@when('anomaly detection is performed with threshold {threshold}')
def when_detect_threshold(context, threshold):
    context.result = detect_anomaly(context.data, float(threshold))


@then('anomaly should be detected')
def then_anomaly(context):
    assert context.result == True


@then('no anomaly should be detected')
def then_no_anomaly(context):
    assert context.result == False
