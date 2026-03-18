class CANBusSimulator:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, signal, value):
        self.messages.append({
            "sender": sender,
            "receiver": receiver,
            "signal": signal,
            "value": value
        })
