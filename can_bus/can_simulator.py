class CANBusSimulator:

    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, signal, value):

        message = {
            "sender": sender,
            "receiver": receiver,
            "signal": signal,
            "value": value
        }

        self.messages.append(message)

    def display_messages(self):

        for msg in self.messages:
            print(msg)
