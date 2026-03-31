Feature: CAN Bus Messaging

  Scenario Outline: Send and validate CAN messages
    Given a CAN bus simulator
    When a message is sent from "<sender>" to "<receiver>" with signal "<signal>" and value <value> and id <id>
    Then the message should be stored
    And the sender should be "<sender>"
    And the receiver should be "<receiver>"
    And the signal should be "<signal>"
    And the value should be <value>
    

    Examples:
      | sender | receiver | signal | value | id   |
      | ECU1   | ECU2     | speed  | 80    | 257  |
      | ECU2   | ECU3     | temp   | 90    | 258  |
