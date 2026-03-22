Feature: Brake System Edge and Negative Scenarios

  Scenario: Brake at zero speed
    Given speed is 0
    When brake is applied with pressure 50
    Then vehicle should remain stationary

  Scenario: Maximum speed braking
    Given speed is 200
    When brake is applied with pressure 80
    Then vehicle should decelerate safely

  Scenario: Invalid negative speed
    Given speed is -50
    When brake is applied with pressure 50
    Then system should raise error

  Scenario: Brake pressure exceeds limit
    Given speed is 80
    When brake is applied with pressure 150
    Then system should reject input

  Scenario: Brake failure
    Given brake system is OFF
    When brake is applied with pressure 70
    Then alert should be triggered

  Scenario: Delayed brake response
    Given response time is 2
    When brake is applied with pressure 60
    Then system should flag delay error

  Scenario: Conflicting signals
    Given accelerator is ON
    And brake is applied with pressure 70
    Then brake should take priority
