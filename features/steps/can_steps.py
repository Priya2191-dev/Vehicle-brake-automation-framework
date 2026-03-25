from behave import given, when, then
from can_bus import CANBusSimulator

@given('a CAN bus simulator')
def given_simulator(context):
    context.simulator = CANBusSimulator()

@when('a message is sent from "{sender}" to "{receiver}" with signal "{signal}" and value {value} and id {msg_id}')
def when_send(context, sender, receiver, signal, value, msg_id):
    context.simulator.send_message(sender, receiver, signal, int(value), int(msg_id))

@then('the message should be stored')
def then_stored(context):
    assert len(context.simulator.messages) > 0

@then('the sender should be "{sender}"')
def then_sender(context, sender):
    assert context.simulator.messages[-1]["sender"] == sender

@then('the receiver should be "{receiver}"')
def then_receiver(context, receiver):
    assert context.simulator.messages[-1]["receiver"] == receiver

@then('the signal should be "{signal}"')
def then_signal(context, signal):
    assert context.simulator.messages[-1]["signal"] == signal

@then('the value should be {value}')
def then_value(context, value):
    assert context.simulator.messages[-1]["value"] == int(value)
