from behave import given, when, then
from src.can_bus import CANBusSimulator   # adjust if your path differs

@given('a CAN bus simulator')
def step_impl(context):
    context.simulator = CANBusSimulator()

@when('a message is sent from "{sender}" to "{receiver}" with signal "{signal}" and value {value}')
def step_impl(context, sender, receiver, signal, value):
    context.simulator.send_message(sender, receiver, signal, int(value))

@then('the message should be stored')
def step_impl(context):
    assert len(context.simulator.messages) == 1

@then('the sender should be "{sender}"')
def step_impl(context, sender):
    assert context.simulator.messages[0]["sender"] == sender

@then('the receiver should be "{receiver}"')
def step_impl(context, receiver):
    assert context.simulator.messages[0]["receiver"] == receiver

@then('the signal should be "{signal}"')
def step_impl(context, signal):
    assert context.simulator.messages[0]["signal"] == signal

@then('the value should be {value}')
def step_impl(context, value):
    assert context.simulator.messages[0]["value"] == int(value)
