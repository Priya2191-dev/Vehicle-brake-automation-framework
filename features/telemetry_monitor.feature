Feature: Telemetry Monitoring

  Scenario: Record telemetry data
    Given a telemetry monitor
    When I record speed 80 and pressure 40
    Then one log should be stored
    And the logged speed should be 80
    And the logged pressure should be 40
