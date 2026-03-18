Feature: CAN Bus Messaging

  Scenario: Send a CAN message successfully
    Given a CAN bus simulator
    When a message is sent from "ECU1" to "ECU2" with signal "speed" and value 80
    Then the message should be stored
    And the sender should be "ECU1"
    And the receiver should be "ECU2"
    And the signal should be "speed"
    And the value should be 80
