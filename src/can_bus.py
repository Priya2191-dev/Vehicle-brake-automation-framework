import logging
import time

logging.basicConfig(level=logging.INFO)

class CANBusSimulator:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, signal, value, message_id):
        """
        Simulates sending a CAN message with validation and logging
        """

        # Validation
        if not sender or not receiver:
            raise ValueError("Sender and Receiver cannot be empty")

        if message_id < 0:
            raise ValueError("Invalid CAN ID")

        message = {
            "id": hex(message_id),  # CAN ID in hex format
            "timestamp": time.time(),
            "sender": sender,
            "receiver": receiver,
            "signal": signal,
            "value": value
        }

        self.messages.append(message)

        logging.info(f"Message Sent: {message}")

    # Filtering by sender
    def get_messages_by_sender(self, sender):
        return [msg for msg in self.messages if msg["sender"] == sender]

    # Display messages
    def display_messages(self):
        for msg in self.messages:
            print(msg)
