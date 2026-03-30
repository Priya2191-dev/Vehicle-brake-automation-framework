Feature: Telemetry Monitoring

  Scenario: Record telemetry data
    Given a telemetry monitor
    When I record speed 80 and pressure 40
    Then one log should be stored
    And the logged speed should be 80
    And the logged pressure should be 40
    And the log should contain a timestamp

  Scenario: Calculate average speed
    Given a telemetry monitor
    When I record multiple telemetry values
    Then the average speed should be 75

  Scenario: Handle invalid input
    Given a telemetry monitor
    When I record invalid telemetry data
    Then an telemetry error should be raised
