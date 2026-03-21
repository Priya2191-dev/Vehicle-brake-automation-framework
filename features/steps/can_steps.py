from behave import given, when, then
from src.can_bus import CANBusSimulator   # adjust if your path differs

@given('a CAN bus simulator')
def given_can_simulator(context):
    context.simulator = CANBusSimulator()

@when('a message is sent from "{sender}" to "{receiver}" with signal "{signal}" and value {value}')
def when_send_message(context, sender, receiver, signal, value):
    context.simulator.send_message(sender, receiver, signal, int(value))

@then('the message should be stored')
def then_verify_message_stored(context):
    assert len(context.simulator.messages) == 1

@then('the sender should be "{sender}"')
def then_verify_sender(context, sender):
    assert context.simulator.messages[0]["sender"] == sender

@then('the receiver should be "{receiver}"')
def then_verify_receiver(context, receiver):
    assert context.simulator.messages[0]["receiver"] == receiver

@then('the signal should be "{signal}"')
def then_verify_signal(context, signal):
    assert context.simulator.messages[0]["signal"] == signal

@then('the value should be {value}')
def then_verify_value(context, value):
    assert context.simulator.messages[0]["value"] == int(value)
