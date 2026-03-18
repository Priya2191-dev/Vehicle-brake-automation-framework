Feature: Brake Simulator

  Scenario: Apply brake reduces speed correctly
    Given a vehicle with speed 100
    When brake is applied with pressure 20
    Then the new speed should be 97

  Scenario: Speed should not go below zero
    Given a vehicle with speed 10
    When brake is applied with pressure 100
    Then the new speed should be 0
